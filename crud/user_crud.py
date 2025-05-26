from sqlalchemy.orm import Session
from models import User
from schemas import UserSchema
from fastapi import HTTPException


def create_user(db: Session, user: UserSchema):
    db_user = db.query(User).filter(User.user_id == user.user_id).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        user_id=user.user_id,
        password=user.password,
        is_admin=user.is_admin
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session, user_id: str):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()
