from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.core.database import Base


class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    platform = Column(String, nullable=False)

    difficulty = Column(String, nullable=False)

    topic = Column(String, nullable=False)

    solved = Column(Boolean, default=False)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )