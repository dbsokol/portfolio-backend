from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class Project(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    name: str
    url: str

    class Config:
        orm_mode = True


class ProjectCreate(BaseModel):
    name: str
    url: str


class ProjectUpdate(BaseModel):
    name: Optional[str]
    url: Optional[str]


class ProjectList(BaseModel):
    count: int
    items: List[Project]
