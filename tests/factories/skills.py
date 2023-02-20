import factory
from app.models.skills import Skill


class SkillFactory(factory.Factory):
    class Meta:
        model = Skill

    name = factory.Faker("job")
    start_date = factory.Faker(
        "date_between",
        start_date="-5y",
        end_date="today",
    )
