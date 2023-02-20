from fastapi.testclient import TestClient

from ..conftest import FixtureSettings


def test_listSkillsIsSuccessful(client: TestClient):
    response = client.get("/skills/")

    assert response.json()["count"] == FixtureSettings.NUMBER_OF_SKILLS


def test_postSkillsIsSuccessful(client: TestClient):
    response = client.post(
        "/skills/",
        json={
            "name": "Skilling",
            "start_date": "2022-01-01",
        },
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Skilling"


def test_getSkillsIsSuccessful(client: TestClient):
    response = client.get("/skills/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_getSkillsFails_whenObjectDoesNotExit(client: TestClient):
    response = client.get("skills/1001")

    assert response.status_code == 404


def test_updateSkillsIsSuccessful(client: TestClient):
    response = client.patch(
        "/skills/1",
        json={
            "name": "Updated Name",
        },
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated Name"


def test_updateSkillsFails_whenSkillIsNotFound(client: TestClient):
    response = client.patch(
        "/skills/1001",
        json={
            "name": "Updated Name",
        },
    )

    assert response.status_code == 404


def test_updateSkillsFails_whenPayloadIsInvalid(client: TestClient):
    response = client.patch(
        "/skills/1",
        json={
            "start_date": "INVALID-VALUE",
        },
    )

    assert response.status_code == 422
