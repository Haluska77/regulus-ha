import requests

class SessionFactory:
    _session = None

    @staticmethod
    def get_session() -> requests.Session:
        if SessionFactory._session is None:
            SessionFactory._session = requests.Session()
        return SessionFactory._session
