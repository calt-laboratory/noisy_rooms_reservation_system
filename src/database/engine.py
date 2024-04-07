from sqlalchemy.engine.base import Engine
from sqlalchemy.engine import create_engine
from src.database.models import Base
from sqlalchemy.orm import sessionmaker

engine: Engine | None = None
DBSession = sessionmaker()


def initialize_database(file: str) -> None:
    """
    Creates database engine and binds it to SQLAlchemy in order to be able to access the database.

    @param file: Path to the database file
    """
    engine = create_engine(url=file)
    Base.metadata.bind = engine
    DBSession.configure(bind=engine)
