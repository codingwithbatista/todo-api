from sqlalchemy import create_engine
from settings.settings_loader import getDatabaseSettings
from sqlalchemy.ext.declarative import declarative_base

database_settings = getDatabaseSettings()
engine = create_engine(database_settings.get_url_connection())
Base = declarative_base()




def create_tables():
    Base.metadata.create_all(engine)
