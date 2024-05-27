from fastapi import HTTPException, status


class DatabaseErrorExc(Exception):
    def __init__(self, message: str = "Database error occurred!"):
        self.message = message
        super().__init__(self.message)


class Auth:
    Unauthorized = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="UNAUTHORIZED")

    @staticmethod
    def scheme_error(scheme: str) -> HTTPException:
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Expected "Bearer" scheme, got {scheme}')
