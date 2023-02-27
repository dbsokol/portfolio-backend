from fastapi import APIRouter, status, Depends, HTTPException

from app.models import skills as models
from app.schemas import skills as schemas
from app.dependencies.databases import get_db


router = APIRouter()


@router.post(
    "/",
    tags=["skills"],
    response_model=schemas.Skill,
    status_code=status.HTTP_201_CREATED,
)
async def create_skill(
    skill_create: schemas.SkillCreate,
    db: get_db = Depends(),
):
    skill = models.Skill(**skill_create.dict())
    db.add(skill)
    db.commit()
    db.refresh(skill)
    return skill


@router.get(
    "/",
    tags=["skills"],
    response_model=schemas.SkillList,
)
async def list_skills(
    db: get_db = Depends(),
):
    skills = db.query(models.Skill).all()
    list_response = schemas.SkillList(
        count=db.query(models.Skill).count(),
        items=skills,
    )
    return list_response


@router.get(
    "/{pk}",
    tags=["skills"],
    response_model=schemas.Skill,
)
async def retrieve_skill(
    pk: int,
    db: get_db = Depends(),
):
    skill = db.query(models.Skill).filter(models.Skill.id == pk).first()
    if not skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"skill with pk={pk} not found",
        )
    return skill


@router.delete(
    "/{pk}",
    tags=["skills"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_skill(
    pk: int,
    db: get_db = Depends(),
):
    db.query(models.Skill).filter(models.Skill.id == pk).delete()
    db.commit()


@router.patch("/{pk}", tags=["skills"], response_model=schemas.Skill)
async def update_skill(
    pk: int,
    skill_update: schemas.SkillUpdate,
    db: get_db = Depends(),
):
    skill = db.query(models.Skill).filter(models.Skill.id == pk).first()
    update_fields = skill_update.dict(exclude_unset=True)

    if not skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"skill with pk={pk} not found",
        )
    try:
        for field, value in update_fields.items():
            setattr(skill, field, value)
        db.commit()
        db.refresh(skill)
    except Exception as exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=[
                f"error when trying to update skill with pk={pk}",
                f"{exception}",
            ],
        )

    return skill
