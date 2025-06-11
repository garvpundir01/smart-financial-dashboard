from pydantic import BaseModel
from datetime import date

class TransactionBase(BaseModel):
    date: date
    description: str
    amount: float
    category: str
    account_id: int

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True
