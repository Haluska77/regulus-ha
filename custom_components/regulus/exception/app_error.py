class AppError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def to_json(self):
        return { "message": self.message }

    @property
    def status_code(self) -> int:
        raise NotImplementedError
