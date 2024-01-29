import httpx
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.testclient import TestClient

from conftest import client
from main import app


#
#
# def test_main_page():
#     response = client.get('/')
#     assert response.status_code == 200
#     assert response.json() == {'message': 'hello world'}
#

@pytest.mark.asyncio
async def test_main_page_async():
    async with AsyncClient(base_url="http://127.0.0.1:8000/") as client:
        response = await client.get('/')
        assert response.status_code == 200
        assert response.json() == {'message': 'hello world'}

