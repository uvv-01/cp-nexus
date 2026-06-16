from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.schemas.user import UserCreate
from app.models.user import User
from app.core.dependencies import get_db
from app.core.security import (
    hash_password,
    verify_password
)
from app.core.auth import create_access_token
from app.core.current_user import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = (
        db.query(User)
        .filter(
            or_(
                User.email == user.email,
                User.username == user.username
            )
        )
        .first()
    )

    if existing_user:
        return {
            "error": "Email or username already registered"
        }

    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(
            user.password
        )
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "id": new_user.id
    }


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    existing_user = (
        db.query(User)
        .filter(
            or_(
                User.email == form_data.username,
                User.username == form_data.username
            )
        )
        .first()
    )

    if not existing_user:
        return {
            "error": "Invalid credentials"
        }

    if not verify_password(
        form_data.password,
        existing_user.password_hash
    ):
        return {
            "error": "Invalid credentials"
        }

    token = create_access_token(
        {"sub": existing_user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/me")
def me(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }