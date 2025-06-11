from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.account import Account as AccountModel
from app.schemas.account_schema import Account, AccountCreate

router = APIRouter()

# Get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create account endpoint
@router.post("/accounts/", response_model=Account)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    db_account = AccountModel(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account
