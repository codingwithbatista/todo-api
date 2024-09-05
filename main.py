from fastapi import FastAPI
from models.models import Todo, create_tables
from repositories.todo_repository import TodoRepository
from resources.todo_resource import todo_resource

app = FastAPI()
app.include_router(todo_resource)
create_tables()


if __name__ == '__main__':
    pass








