from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic

demo_auth_router = APIRouter(prefix='/demo-auth', tags=['Demo Auth'])


security = HTTPBasic()


@demo_auth_router.get('/basic-auth')
def demo_basic_auth_credentials(
        credential: Annotated[HTTPBasicCredentials, Depends(security)]
):

    return {
        'message': 'Hi!',
        'username': credential.username,
        'password': credential.password
    }