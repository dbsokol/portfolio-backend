from fastapi import APIRouter, status, Depends, HTTPException

from ..models import projects as models
from ..schemas import projects as schemas
from ..dependencies.databases import get_db


router = APIRouter()


@router.post(
    "/",
    tags=["projects"],
    response_model=schemas.Project,
    status_code=status.HTTP_201_CREATED,
)
async def create_project(
    project_create: schemas.ProjectCreate,
    db: get_db = Depends(),
):
    project = models.Project(**project_create.dict())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


@router.get(
    "/",
    tags=["projects"],
    response_model=schemas.ProjectList,
)
async def list_projects(
    db: get_db = Depends(),
):
    projects = db.query(models.Project).all()
    list_response = schemas.ProjectList(
        count=db.query(models.Project).count(),
        items=projects,
    )
    return list_response


@router.get(
    "/{pk}",
    tags=["projects"],
    response_model=schemas.Project,
)
async def retrieve_project(
    pk: int,
    db: get_db = Depends(),
):
    project = db.query(models.Project).filter(models.Project.id == pk).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"project with pk={pk} not found",
        )
    return project


@router.delete(
    "/{pk}",
    tags=["projects"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_project(
    pk: int,
    db: get_db = Depends(),
):
    db.query(models.Project).filter(models.Project.id == pk).delete()
    db.commit()


@router.patch("/{pk}", tags=["projects"], response_model=schemas.Project)
async def update_project(
    pk: int,
    project_update: schemas.ProjectUpdate,
    db: get_db = Depends(),
):
    project = db.query(models.Project).filter(models.Project.id == pk).first()
    update_fields = project_update.dict(exclude_unset=True)

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"project with pk={pk} not found",
        )
    try:
        for field, value in update_fields.items():
            setattr(project, field, value)
        db.commit()
        db.refresh(project)
    except Exception as exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=[
                f"error when trying to update project with pk={pk}",
                f"{exception}",
            ],
        )

    return project
