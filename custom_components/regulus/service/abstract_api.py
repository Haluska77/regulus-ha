from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any, Dict
from .session_factory import SessionFactory
from .login_service import LoginService
from ..config.config import HOST
from .xml_parser_service import parse_xml_to_map
from ..exception.conflict_error import ConflictError

T = TypeVar('T')

class AbstractApi(Generic[T], ABC):
    page: str
    
    def __init__(self):
        self.session = SessionFactory.get_session()

    def route_fetch(self):
        try:
            data = self.fetch()
            print(f"Data ", data.json())

            return data.json()
        except ConflictError as error:
            return str(error)
        except Exception as error:
            raise error  # To be handled by a global error handler

    def fetch(self) -> Any:
        api_url = f"{HOST}{self.page}"
        return self.execute(lambda: self.session.get(api_url, allow_redirects=False))

    def execute(self, operation) -> Any:
        while True:
            response = operation()
            # print(f"Session Cookie", self.session.cookies.get_dict())
            # print(f"Status Code: {response.status_code}")
            # print(f"Headers:\n{response.headers}")
            # print(f"Body:\n{response.text}")
            if response.status_code == 200:
                return self.get_response(response.text)
            print("Redirect detected, re-authenticating...")

            login_service = LoginService()
            login_service.success_login(response)

    def get_response(self, data: str) -> Any:
        if not data:
            raise ConflictError("No data received from the API")
        schema_xml_map = parse_xml_to_map(data)
        registry_errors = []

        response = self.generate_response(schema_xml_map, registry_errors)

        if registry_errors:
            raise ConflictError("|".join(registry_errors))

        return response

    @abstractmethod
    def generate_response(self, schema_xml_map: Dict[str, str], registry_errors: list) -> Any:
        pass
