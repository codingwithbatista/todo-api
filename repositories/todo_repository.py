from typing import override
from repositories.repository import Repository
from models.models import Todo

class TodoRepository(Repository):

  def __init__(self):
    pass

  def insert(self, title: str, description: str, priority: int, complete: bool = False) -> None:
    super().insert(Todo(title=title, description=description, priority=priority, complete=complete))



  @override
  def query_by_id(self, id: int) -> Todo:
      session = super().get_session()
      result = session.query(Todo).filter_by(id = id).first()
      session.close()
      return result

  @override
  def query_all(self):
     session = super().get_session()
     result = session.query(Todo).all()
     session.close()
     return result

  def query_by_priority(self, priority) -> list[Todo]:
      session = super().get_session()
      result = session.query(Todo).filter_by(priority = priority).all()
      session.close()
      return result




