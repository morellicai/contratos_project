from http import HTTPStatus

from fastapi.testclient import TestClient

from contratos_project.app import app


def test_root_deve_retornar_ok():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
