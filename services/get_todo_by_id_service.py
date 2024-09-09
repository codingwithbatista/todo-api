from models.to_do import Todo
from models.response.todo_response import TodoResponse
from services.todo_service import TodoService


class GetTodoByIdService(TodoService):

    def __init__(self) -> None:
        super().__init__()



    def execute(self, id: int) -> TodoResponse:
        todo: Todo = self.todo_repository.query_by_id(id)
        return self.to_response(todo)


