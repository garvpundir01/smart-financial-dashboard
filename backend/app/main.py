from fastapi import FastAPI
from app.database import Base, engine
from app.routes import account_routes
from app.routes import transaction_routes
from app.models import account, transaction



app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Smart Finance Dashboard Backend is working!"}

# Connect the account API
app.include_router(account_routes.router)

app.include_router(transaction_routes.router)
