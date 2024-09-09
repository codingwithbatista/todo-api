from sqlalchemy import Boolean, Column, Integer, String
from models import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    description = Column(String(100), default="", nullable=False)
    priority = Column(Integer, nullable=False)
    complete = Column(Boolean, default=False, nullable=False)
