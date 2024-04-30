from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_register():
    response = client.post(
        "http://127.0.0.1:8000/api/v1/auth/register",
        json={
            "email": "test_user20@example.com",
            "password": 'qwerty',
            "is_active": True,
            "is_superuser": False,
            "is_verified": False,
            "username": "test_user20"
        }
    )
    
    if response.status_code == 201:
        print("Пользователь успешно зарегистрирован")
        assert True
    elif response.status_code == 400:
        print('Пользователь с такими данными уже существует.')
        assert False
    else:
        assert False
