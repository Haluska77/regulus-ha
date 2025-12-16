import logging
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any, Dict

from ..const import IR_VERSION_ALIASES
from .session_factory import SessionFactory
from .login_service import LoginService
from .xml_parser_service import parse_xml_to_map
from importlib import import_module
from urllib.parse import urlencode

T = TypeVar('T')
registry_mapper: Dict[str, str] = {}

_LOGGER = logging.getLogger(__name__)

class AbstractApi(Generic[T], ABC):
    page: str
    
    def __init__(self, config: dict):
        self.config = config      
        self.session = SessionFactory.get_session()
        self.host = config["host"]
        self.url = f"http://{self.host}"
        self.mapper = self.load_registry_mapper_by_version(config["ir_version"])

    def route_fetch(self):
        return self.fetch()

    def fetch(self) -> Any:
        api_url = f"{self.url}{self.page}"
        try:
            return self.execute(lambda: self.session.get(api_url, allow_redirects=False))
        except Exception as e:
            raise ValueError(f"Failed to fetch") from e
    
    def route_update(self, body: Dict[str, Any]) -> Any:
        return self.update(body)

    def update(self, body: Dict[str, Any]) -> Any:
        def send_request():
            api_url = f"{self.url}{self.page}"
            body_obj = self.object_to_urlencoded(body)
            try:
                resp = self.session.post(
                    api_url,
                    data=body_obj,
                    headers={"Content-Type": "application/x-www-form-urlencoded"},
                    allow_redirects=False
                )
                resp.raise_for_status()
                return resp
            except Exception as e:
                raise ValueError(f"Failed to update") from e
        
        return self.execute(send_request)
    
    def object_to_urlencoded(self, req_body: Dict[str, Any]) -> str:
        encoded_body = {}

        for api_registry_key, value in req_body.items():
            registry_name = self.mapper.get(api_registry_key)
            if registry_name and value is not None:
                if isinstance(value, bool):
                    encoded_body[registry_name] = "1" if value else "0"
                else:
                    encoded_body[registry_name] = str(value)
        return urlencode(encoded_body)
    
    def execute(self, operation) -> Any:
        while True:
            response = operation()
            if response.status_code == 200:
                return self.get_response(response.text)

            login_service = LoginService(self.config)
            login_service.success_login(response)

    def get_response(self, data: str) -> Any:
        try:
            schema_xml_map = parse_xml_to_map(data)
            response = self.generate_response(schema_xml_map, self.mapper)

            return response.dict()
        except Exception as e:
            raise ValueError(f"Failed to parse response") from e

    def load_registry_mapper_by_version(self, raw_ir_version: any) -> Dict[str, str]:
        try:
            ir_version = IR_VERSION_ALIASES[raw_ir_version]
        except KeyError:
            raise ValueError(f"Unsupported ir_version: {raw_ir_version}")

        module_name = (
            f"custom_components.regulus.mapper.registry_mapper_ir{ir_version}"
        )

        try:
            module = import_module(module_name)
        except ModuleNotFoundError as err:
            raise ValueError(f"No registry mapper for ir_version: {ir_version}") from err

        return module.REGISTRY_MAPPER

    @abstractmethod
    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> Any:
        pass