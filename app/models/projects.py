from sqlalchemy import Column, String
from .base import BaseModel


class Project(BaseModel):
    __tablename__ = "projects"

    name = Column(String, index=True)
    url = Column(String)
