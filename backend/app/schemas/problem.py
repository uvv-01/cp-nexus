from pydantic import BaseModel


class ProblemCreate(BaseModel):
    title: str
    platform: str
    difficulty: str
    topic: str