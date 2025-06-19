from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any, Dict
from .session_factory import SessionFactory
from .login_service import LoginService
from .xml_parser_service import parse_xml_to_map
from ..exception.conflict_error import ConflictError
from importlib import import_module

T = TypeVar('T')

class AbstractApi(Generic[T], ABC):
    page: str
    
    def __init__(self, config: dict):
        self.config = config      
        self.session = SessionFactory.get_session()
        self.host = config["host"]
        self.url = f"http://{self.host}"

    def route_fetch(self):
        try:
            return self.fetch()
        except Exception as error:
            return {"error": f"Unhandled error: {str(error)}"}

    def fetch(self) -> Any:
        api_url = f"{self.url}{self.page}"
        return self.execute(lambda: self.session.get(api_url, allow_redirects=False))

    def execute(self, operation) -> Any:
        while True:
            response = operation()
            if response.status_code == 200:
                return self.get_response(response.text)
            print("Redirect detected, re-authenticating...")

            login_service = LoginService(self.config)
            login_service.success_login(response)

    def get_response(self, data: str) -> Any:
        if not data:
            raise ConflictError("No data received from the API")
        schema_xml_map = parse_xml_to_map(data)

        registry_mapper = self.load_registry_mapper_by_version(self.config["ir_version"])
        response = self.generate_response(schema_xml_map, registry_mapper)

        return response.dict()

    def load_registry_mapper_by_version(self, ir_version: int) -> Dict[str, str]:

        version_map = {
            12: "custom_components.regulus.mapper.registry_mapper_ir12",
            14: "custom_components.regulus.mapper.registry_mapper_ir14",
        }

        module_name = version_map.get(ir_version)
        if not module_name:
            raise ValueError(f"Unsupported ir_version: {ir_version}")

        module = import_module(module_name)
        return module.REGISTRY_MAPPER

    @abstractmethod
    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> Any:
        pass