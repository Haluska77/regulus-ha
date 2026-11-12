import requests
from typing import Dict
from urllib.parse import urlparse
from .session_factory import SessionFactory
from .xml_parser_service import parse_acer_value

# The controller is slow but must never block an executor thread forever.
REQUEST_TIMEOUT = 10


def is_login_redirect(url: str) -> bool:
    """Firmwares redirect unauthenticated requests either to /LOGIN.XML or,
    like IR14 1.0.11.30, to an absolute http://<host>/LOGIN.HTM."""
    path = urlparse(url).path.upper()
    return path.endswith("/LOGIN.XML") or path.endswith("/LOGIN.HTM")


class LoginService:

    def __init__(self, config: dict):
        self.host = config["host"]
        self.url = f"http://{self.host}/login.xml"
        self.user = config["user"]
        self.password = config["password"]
        self.session = SessionFactory.get_session()

    def login_url_for(self, redirect_url: str) -> str:
        # LOGIN.HTM is a JS page; its form posts to the TECO system endpoint.
        if urlparse(redirect_url).path.upper().endswith("/LOGIN.HTM"):
            return f"http://{self.host}/syswww/LOGIN.XML"
        return self.url

    def get_login(self) -> requests.Response:
        return self.session.get(self.url, timeout=REQUEST_TIMEOUT)

    def post_login(self, url: str = None) -> requests.Response:

        login_data: Dict[str, str] = {
            "USER": self.user,
            "PASS": self.password,
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        return self.session.post(url or self.url, data=login_data, headers=headers,
                                 allow_redirects=False, timeout=REQUEST_TIMEOUT)

    def success_login(self, response: requests.Response) -> str:
        login_status = response.status_code
        redirect_url = response.headers.get("Location", "")
        count = 1

        while count < 10 and login_status == 302 and is_login_redirect(redirect_url):
            login_response = self.post_login(self.login_url_for(redirect_url))
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
