from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.config import config
from app.exc import Auth


def bearer_auth(token: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())]):
    scheme = token.scheme
    if scheme != "Bearer":
        raise Auth.scheme_error(scheme)
    if token.credentials != config.API_TOKEN:
        raise Auth.Unauthorized
