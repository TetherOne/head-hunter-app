from httpx import AsyncClient

from main import app



async def test_register():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000/api/v1/auth") as ac:
        response = await ac.post(
            "/register",
            json={
                "email": "test_user8@example.com",
                "password": "qwerty",
                "is_active": True,
                "is_superuser": False,
                "is_verified": False,
                "username": "test_user8"
            }
        )

        assert response.status_code == 201
