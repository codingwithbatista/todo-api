from fastapi import FastAPI
from models.models import create_tables

app = FastAPI()

create_tables()






