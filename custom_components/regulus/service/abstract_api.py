from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any, Dict
from .session_factory import SessionFactory
from .login_service import LoginService
from .xml_parser_service import parse_xml_to_map
from ..exception.conflict_error import ConflictError

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
        except ConflictError as error:
            return {"error": str(error)}
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
        registry_errors = []

        response = self.generate_response(schema_xml_map, registry_errors)

        if registry_errors:
            raise ConflictError("|".join(registry_errors))

        return response.dict()

    @abstractmethod
    def generate_response(self, schema_xml_map: Dict[str, str], registry_errors: list) -> Any:
        pass