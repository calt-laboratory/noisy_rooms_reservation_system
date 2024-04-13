from typing import Protocol, Any

from src.database.engine import DBSession
from src.database.models import Base, convert_to_dict

DataObject = dict[str, Any]


class DBInterface(Protocol):

    def __init__(self, db_class: type[Base]) -> None:
        self.db_class = db_class

    def read_by_id(self, id: int) -> DataObject:
        session = DBSession()
        result = session.quey(self.db_class).get(id)
        return convert_to_dict(result)

    def read_all(self) -> list[DataObject]:
        session = DBSession()
        results = session.query(self.db_class).all()
        return [convert_to_dict(result) for result in results]

    def create(self, data: DataObject) -> DataObject:
        session = DBSession()
        result = self.db_class(**data)
        session.add(result)
        session.commit()
        return convert_to_dict(result)

    def update(self, id: int, data: DataObject) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)
        for key, value in data.items():
            setattr(result, key, value)
        session.commit()
        return convert_to_dict(result)

    def delete(self, id: int) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)
        session.delete(result)
        session.commit()
        return convert_to_dict(result)
