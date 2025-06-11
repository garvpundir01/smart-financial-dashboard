from fastapi import FastAPI
from app.database import Base, engine

app = FastAPI()

# This line creates all tables based on the models
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Smart Finance Dashboard Backend is working!"}
