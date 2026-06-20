from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.task import router as task_router
from app.core.database import Base, engine
from app.models.user import User
from app.api.problem import router as problem_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CP Nexus")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(auth_router)
app.include_router(auth_router)
app.include_router(task_router)
app.include_router(problem_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "CP Nexus Running"}