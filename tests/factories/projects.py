import factory
from app.models.projects import Project


class ProjectFactory(factory.Factory):
    class Meta:
        model = Project

    name = factory.Faker("job")
    url = factory.Faker('url')
