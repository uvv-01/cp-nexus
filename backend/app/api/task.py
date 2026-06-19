from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.current_user import get_current_user
from app.models.user import User
from app.models.task import Task
from app.schemas.task import TaskCreate

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

# GET all tasks
@router.get("/")
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    tasks = (
        db.query(Task)
        .filter(Task.user_id == current_user.id)
        .all()
    )

    return tasks


# CREATE task
@router.post("/")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_task = Task(
        title=task.title,
        user_id=current_user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "message": "Task created successfully",
        "id": new_task.id
    }
@router.patch("/{task_id}")
def update_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.user_id == current_user.id
        )
        .first()
    )

    if not task:
        return {"error": "Task not found"}

    task.completed = True

    db.commit()
    db.refresh(task)

    return {
        "message": "Task marked as completed"
    }
@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.user_id == current_user.id
        )
        .first()
    )

    if not task:
        return {"error": "Task not found"}

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted successfully"
    }