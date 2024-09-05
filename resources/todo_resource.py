from fastapi import APIRouter

from models.models import Todo
from models.response.todo_response import TodoResponse
from services.get_all_todos_service import GetAllTodosService
from services.get_todo_by_id_service import GetTodoByIdService

get_all_todos_service = GetAllTodosService()
get_todo_by_id_service= GetTodoByIdService()
todo_resource = APIRouter(prefix="/todo-api")


@todo_resource.get("/")
async def get_all_todos() -> list[TodoResponse]:
    return get_all_todos_service.execute()

@todo_resource.get("/{todo_id}")
async def get_by_id(todo_id: int) -> TodoResponse:
    return get_todo_by_id_service.execute(todo_id)
