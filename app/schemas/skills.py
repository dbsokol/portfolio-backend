from pydantic import BaseModel
from datetime import date, datetime
from typing import List, Optional


class Skill(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    name: str
    start_date: date

    class Config:
        orm_mode = True


class SkillCreate(BaseModel):
    name: str
    start_date: date


class SkillUpdate(BaseModel):
    name: Optional[str]
    start_date: Optional[date]


class SkillList(BaseModel):
    count: int
    items: List[Skill]
