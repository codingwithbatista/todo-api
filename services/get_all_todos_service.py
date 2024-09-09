
from models.to_do import Todo
from models.response.todo_response import TodoResponse
from repositories.todo_repository import TodoRepository
from services.todo_service import TodoService


class GetAllTodosService(TodoService):

    def __init__(self) -> None:
        super().__init__()



    def execute(self) -> list[TodoResponse]:
        todos: list[Todo] = self.todo_repository.query_all()
        return self.all_to_response(todos)



