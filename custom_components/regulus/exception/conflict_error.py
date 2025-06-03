from .app_error import AppError

class ConflictError(AppError):
    @property
    def status_code(self) -> int:
        return 409

    def __init__(self, message="Conflict occurred"):
        super().__init__(message)
