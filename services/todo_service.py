from models.to_do import Todo
from models.response.todo_response import TodoResponse
from repositories.todo_repository import TodoRepository


class TodoService():
    __todo_repository: TodoRepository

    def __init__(self) -> None:
        self.__todo_repository = TodoRepository()


    @property
    def todo_repository(self) -> TodoRepository:
        return self.__todo_repository

    @todo_repository.setter
    def todo_repository(self, value:TodoRepository):
        self.__todo_repository = value


    def to_response(self, todo: Todo) -> TodoResponse:
        json:dict = todo.__dict__
        return TodoResponse(id=int(json['id']), title=str(json['title']),
                            description=str(json['description']), priority=int(json['priority']),
                            complete=bool(json['complete']))

    def all_to_response(self, todos: list[Todo]) -> list[TodoResponse]:
        result: list[TodoResponse] = []
        for element in todos:
            result.append(self.to_response(element))
        return result
