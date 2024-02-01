from fastapi.testclient import TestClient

from main import app



client = TestClient(app)



def test_create_resume():
    response = client.post(
        "http://127.0.0.1:8000/api/v1/resume",
        json={
          "user_id": 29,
          "job_name": 'водила',
          "skills": 'быстро еду',
          "experience": "10 лет",
          "salary": 100000
        }
    )

    if response.status_code == 201:

        assert True

    else:

        print('Неправильная валидация данных при создании резюме.')
        assert False
