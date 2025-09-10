from fastapi import FastAPI
from backend import models
from backend.database import engine

app = FastAPI()

# create tables in database
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Setup": "Success"}


