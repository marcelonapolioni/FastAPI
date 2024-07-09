from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user():
    client = TestClient(app)

    response = client.post(
        "/users/",
        json={
            "username": "testusername",
            "password": "password",
            "email": "test@test.com",
        },
    )

    # Verifiação se o status coderetornado é o correto
    assert response.status_code == HTTPStatus.CREATED

    # Validação so UserPublic
    assert response.json() == {
        "username": "testusername",
        "email": "test@test.com",
        "id": 1,
    }
