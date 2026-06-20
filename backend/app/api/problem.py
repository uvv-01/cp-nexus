from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.current_user import get_current_user
from app.models.user import User
from app.models.problem import Problem
from app.schemas.problem import ProblemCreate

router = APIRouter(
    prefix="/problems",
    tags=["Problems"]
)
@router.post("/")
def create_problem(
    problem: ProblemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_problem = Problem(
        title=problem.title,
        platform=problem.platform,
        difficulty=problem.difficulty,
        topic=problem.topic,
        user_id=current_user.id
    )

    db.add(new_problem)
    db.commit()
    db.refresh(new_problem)

    return {
        "message": "Problem added successfully",
        "id": new_problem.id
    }
@router.get("/")
def get_problems(
    difficulty: str | None = None,
    platform: str | None = None,
    topic: str | None = None,
    solved: bool | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = (
        db.query(Problem)
        .filter(
            Problem.user_id == current_user.id
        )
    )

    if difficulty:
        query = query.filter(
            Problem.difficulty == difficulty
        )

    if platform:
        query = query.filter(
            Problem.platform == platform
        )

    if topic:
        query = query.filter(
            Problem.topic == topic
        )

    if solved is not None:
        query = query.filter(
            Problem.solved == solved
        )

    return query.all()
@router.patch("/{problem_id}")
def update_problem(
    problem_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    problem = (
        db.query(Problem)
        .filter(
            Problem.id == problem_id,
            Problem.user_id == current_user.id
        )
        .first()
    )

    if not problem:
        return {
            "error": "Problem not found"
        }

    problem.solved = True

    db.commit()

    return {
        "message": "Problem marked as solved"
    }
@router.delete("/{problem_id}")
def delete_problem(
    problem_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    problem = (
        db.query(Problem)
        .filter(
            Problem.id == problem_id,
            Problem.user_id == current_user.id
        )
        .first()
    )

    if not problem:
        return {
            "error": "Problem not found"
        }

    db.delete(problem)
    db.commit()

    return {
        "message": "Problem deleted successfully"
    }