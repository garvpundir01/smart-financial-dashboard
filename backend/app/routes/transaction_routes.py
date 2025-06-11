from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.transaction import Transaction as TransactionModel
from app.schemas.transaction_schema import Transaction, TransactionCreate
from typing import List
from fastapi import Query
from collections import defaultdict
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/transactions/", response_model=Transaction)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = TransactionModel(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@router.get("/transactions/", response_model=List[Transaction])
def get_transactions(account_id: int = Query(None), db: Session = Depends(get_db)):
    if account_id:
        return db.query(TransactionModel).filter(TransactionModel.account_id == account_id).all()
    return db.query(TransactionModel).all()

@router.get("/transactions/summary/{account_id}")
def get_transaction_summary(account_id: int, db: Session = Depends(get_db)):
    transactions = db.query(TransactionModel).filter(TransactionModel.account_id == account_id).all()

    total_income = sum(t.amount for t in transactions if t.amount > 0)
    total_expenses = sum(abs(t.amount) for t in transactions if t.amount < 0)
    net_balance = total_income - total_expenses

    return {
        "account_id": account_id,
        "total_income": round(total_income, 2),
        "total_expenses": round(total_expenses, 2),
        "net_balance": round(net_balance, 2)
    }

@router.get("/transactions/category-summary/{account_id}")
def get_category_summary(account_id: int, db: Session = Depends(get_db)):
    transactions = db.query(TransactionModel).filter(TransactionModel.account_id == account_id).all()

    category_totals = defaultdict(float)

    for t in transactions:
        category_totals[t.category] += t.amount

    # Format and round
    formatted = [
        {"category": cat, "total": round(total, 2)}
        for cat, total in category_totals.items()
    ]

    return {"account_id": account_id, "categories": formatted}

@router.get("/transactions/monthly-summary/{account_id}")
def get_monthly_summary(account_id: int, db: Session = Depends(get_db)):
    transactions = db.query(TransactionModel).filter(TransactionModel.account_id == account_id).all()

    monthly_totals = defaultdict(float)

    for t in transactions:
        month = t.date.strftime("%Y-%m")  # e.g., "2025-06"
        monthly_totals[month] += t.amount

    formatted = [
        {"month": m, "total": round(t, 2)}
        for m, t in sorted(monthly_totals.items())
    ]

    return {"account_id": account_id, "monthly": formatted}
