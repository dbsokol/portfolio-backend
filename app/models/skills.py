from sqlalchemy import Column, String, Date
from .base import BaseModel


class Skill(BaseModel):
    __tablename__ = "skills"

    name = Column(String, index=True)
    start_date = Column(Date)
