from models import engine
from sqlalchemy.orm import Session

class Repository:

    def get_session(self):
        session = Session(bind=engine)
        return session

    def insert(self, data):
        session = self.get_session()
        session.add(data)
        session.commit()
        session.close()

    def insert_all(self, data:list[any]):
        session = self.get_session()
        session.bulk_save_objects(data)
        session.comit()
        session.close()

    def query_by_id(self, id: int):
        raise NotImplementedError("Please implement this method")

    def query_all(self):
        raise NotImplementedError("Please implement this method")
