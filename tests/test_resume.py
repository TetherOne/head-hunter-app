from fastapi.testclient import TestClient

from main import app



client = TestClient(app)



# def test_create_resume():
#     response = client.post(
#         "http://127.0.0.1:8000/api/v1/resume",
#         json={
#           "user_id": 29,
#           "job_name": 'водила',
#           "skills": 'быстро еду',
#           "experience": "10 лет",
#           "salary": 100000
#         }
#     )
#
#     if response.status_code == 201:
#
#         assert True
#
#     else:
#
#         print('Неправильная валидация данных при создании резюме.')
#         assert False


# def test_update_resume():
#     resume_id = 25
#     response = client.put(
#         f'http://127.0.0.1:8000/api/v1/resume/{resume_id}',
#         json={
#             "user_id": 24,
#             "job_name": 'шахтер вася пупкин',
#             "skills": 'быстро копаю',
#             "experience": "10 лет",
#             "salary": 10000,
#         }
#     )
#
#     if response.status_code == 200:
#
#         assert True
#
#     else:
#
#         print('Неправильная валидация данных при обновлении резюме.')
#         assert False



def test_update_resume_partial():
    resume_id = 25
    response = client.patch(
        f'http://127.0.0.1:8000/api/v1/resume/{resume_id}',
        json={
            "skills": False
        }
    )

    if response.status_code == 200:

        assert True

    else:

        print('Неправильная валидация данных при обновлении резюме.')
        assert False