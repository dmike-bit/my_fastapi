import re

from fastapi import FastAPI
from database import Base, engine, SessionLocal
import models
from models import User

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/users")
def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users