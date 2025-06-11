from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from app.database import Base
from datetime import date

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, default=date.today)
    description = Column(String)
    amount = Column(Float)
    category = Column(String)
    account_id = Column(Integer, ForeignKey("accounts.id"))  # links to Account
