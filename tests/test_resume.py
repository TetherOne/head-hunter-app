import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture
def ac():
    return AsyncClient()


@pytest.mark.asyncio
async def test_create_resume(ac: AsyncClient):
    response = await ac.post('http://127.0.0.1:8000/resume', json={
        "user_id": 2,
        "job_name": "прогер",
        "skills": "питон",
        "experience": "10 лет",
        "salary": 10000
    })

    assert response.status_code == 201