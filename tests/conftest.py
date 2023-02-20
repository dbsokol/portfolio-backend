import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session
from sqlmodel.pool import StaticPool

from app.main import app
from app.dependencies.databases import get_db
from app.models.base import BaseModel

from .factories.skills import SkillFactory
from .factories.projects import ProjectFactory


class FixtureSettings:
    NUMBER_OF_SKILLS = 10
    NUMBER_OF_PROJECTS = 10


def load_fixtures(session):
    skills = SkillFactory.build_batch(size=FixtureSettings.NUMBER_OF_SKILLS)
    session.bulk_save_objects(skills)
    projects = ProjectFactory.build_batch(
        size=FixtureSettings.NUMBER_OF_PROJECTS
    )
    session.bulk_save_objects(projects)
    session.commit()


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    BaseModel.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    BaseModel.metadata.drop_all(bind=engine)


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_db] = get_session_override

    load_fixtures(session)

    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()
