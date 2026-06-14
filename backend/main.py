from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.core.database import Base, engine
from app.models.user import User

app = FastAPI(title="CP Nexus")
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "CP Nexus Running"}