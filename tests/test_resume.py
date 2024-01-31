from httpx import AsyncClient

from main import app



async def test_create_resume():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000/api/v1") as ac:
        response = await ac.post(
            "/resume",
            json={
              "user_id": 19,
              "job_name": "дворник",
              "skills": "мести дорогу",
              "experience": "20 лет",
              "salary": 121212
            }
        )

        assert response.status_code in {201, 307}