# Routes/user.py
from fastapi import APIRouter, Depends, HTTPException
from model.user import User
from Validators.user_validator import UserCreateSchema
from config.db import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text
router = APIRouter()

@router.post("/user")
async def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(username=user.username, email=user.email, password=user.password)

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        db.rollback()

        raise HTTPException(status_code=400, detail="User could not be created")
    
    return {"message": "User created", "user": new_user}


@router.get("/user/all")
async def get_all_users(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM users")).fetchall()  
    return {"users": result}