from fastapi.testclient import TestClient

from ..conftest import FixtureSettings


def test_listProjectsIsSuccessful(client: TestClient):
    response = client.get("/projects/")

    assert response.json()["count"] == FixtureSettings.NUMBER_OF_SKILLS


def test_postProjectsIsSuccessful(client: TestClient):
    response = client.post(
        "/projects/",
        json={
            "name": "My First Project",
            "url": "https://some-url.com",
        },
    )

    assert response.status_code == 201
    assert response.json()["name"] == "My First Project"


def test_getProjectsIsSuccessful(client: TestClient):
    response = client.get("/projects/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_getProjectsFails_whenObjectDoesNotExit(client: TestClient):
    response = client.get("projects/1001")

    assert response.status_code == 404


def test_updateProjectsIsSuccessful(client: TestClient):
    response = client.patch(
        "/projects/1",
        json={
            "name": "Updated Name",
        },
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated Name"


def test_updateProjectsFails_whenProjectIsNotFound(client: TestClient):
    response = client.patch(
        "/projects/1001",
        json={
            "name": "Updated Name",
        },
    )

    assert response.status_code == 404
