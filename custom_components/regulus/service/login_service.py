import requests
from typing import Dict
from .session_factory import SessionFactory
from ..config.config import HOST, USER, PASSWORD
from .xml_parser_service import parse_acer_value
# from ..exception.unauthorized_error import UnAuthorizedError
# from ..exception.illegal_status_error import IllegalStatusError


class LoginService:
    URL = f"{HOST}/login.xml"

    def __init__(self):
        self.session = SessionFactory.get_session()

    def get_login(self) -> requests.Response:
        return self.session.get(self.URL)

    def post_login(self) -> requests.Response:

        login_data: Dict[str, str] = {
            "USER": USER,
            "PASS": PASSWORD,
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        return self.session.post(self.URL, data=login_data, headers=headers, allow_redirects=False)

    def success_login(self, response: requests.Response) -> str:
        login_status = response.status_code
        redirect_url = response.headers.get("Location", "")
        count = 1

        while count < 10 and login_status == 302 and redirect_url.upper() == "/LOGIN.XML":
            login_response = self.post_login()
            login_status = login_response.status_code

            if login_status == 200 and login_response.text:
                self.validate_login_status(login_response.text)

            redirect_url = login_response.headers.get("Location", "/home.xml")
            print(f"Logged in and redirect to {redirect_url}")
            count += 1

        return redirect_url

    def validate_login_status(self, data: str):
        acer_value = parse_acer_value(data)
        print(f"Login error {acer_value}")

        # if acer_value == "1":
        #     raise UnAuthorizedError()
        # else:
        #     raise IllegalStatusError()
