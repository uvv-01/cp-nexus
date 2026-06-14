from fastapi import FastAPI

from app.core.database import Base, engine
from app.models.user import User

app = FastAPI(title="CP Nexus")

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "CP Nexus Running"}