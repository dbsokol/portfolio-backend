from fastapi import FastAPI
from .routers import skills
from .routers import projects
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.include_router(
    skills.router,
    prefix="/skills",
    tags=["skills"],
)
app.include_router(
    projects.router,
    prefix="/projects",
    tags=["projects"],
)
app.mount(
    "/coverage",
    StaticFiles(
        directory="htmlcov",
        html=True,
    ),
    name="coverage",
)


@app.get("/")
async def root():
    return 200
