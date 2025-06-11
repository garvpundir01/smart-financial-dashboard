from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)       # e.g., "Checking Account"
    type = Column(String)                        # e.g., "Bank", "Credit Card"
    balance = Column(Float)                      # e.g., 1234.56
