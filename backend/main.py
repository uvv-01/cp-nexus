from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.task import router as task_router
from app.core.database import Base, engine
from app.models.user import User
from app.api.problem import router as problem_router

app = FastAPI(title="CP Nexus")
app.include_router(auth_router)
app.include_router(auth_router)
app.include_router(task_router)
app.include_router(problem_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "CP Nexus Running"}