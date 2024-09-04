from sqlalchemy import Boolean, Column, Integer, String, create_engine
from settings.settings_loader import getDatabaseSettings
from sqlalchemy.ext.declarative import declarative_base


__database_settings = getDatabaseSettings()
__engine = create_engine(__database_settings.get_url_connection())
__base = declarative_base()


def create_tables():
    __base.metadata.create_all(__engine)


class Todo(__base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    description = Column(String(100), default="", nullable=False)
    priority = Column(Integer, nullable=False)
    complete = Column(Boolean, default=False, nullable=False)
