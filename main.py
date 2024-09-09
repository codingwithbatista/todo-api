from fastapi import FastAPI
from models import create_tables
from resources.todo_resource import todo_resource
from resources.auth_resource import auth_resource

app = FastAPI()
app.include_router(todo_resource)
app.include_router(auth_resource)
create_tables()


if __name__ == '__main__':
    pass








