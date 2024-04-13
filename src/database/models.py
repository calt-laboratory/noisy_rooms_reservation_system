from typing import Any

from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date, Integer, String

Base = declarative_base()


def convert_to_dict(obj: Base) -> dict[str, Any]:
    result_dict = {}
    for column in obj.__table__.columns:
        column_value = getattr(obj, column.name)
        result_dict[column.name] = column_value
    return result_dict


class DBNoisician(Base):
    __tablename__ = "noisician"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email_address = Column(String(250), nullable=False)


class DBNoisyRoom(Base):
    __tablename__ = "noisy_room"
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String(250), nullable=False)
    size = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)


class DBBooking(Base):
    __tablename__ = "booking"
    id = Column(Integer, primary_key=True, autoincrement=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)

    noisician_id = Column(Integer, ForeignKey("noisician.id"))
    noisician = relationship(DBNoisician)
    noisy_room_id = Column(Integer, ForeignKey("noisy_room.id"))
    noisy_room = relationship(DBNoisyRoom)
