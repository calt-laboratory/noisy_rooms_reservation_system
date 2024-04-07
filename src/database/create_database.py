from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.database.models import Base
from src.database.sample_data import customers, noisy_rooms


def create_database(file: str) -> None:
    engine = create_engine(url=file)
    Base.metadata.create_all(bind=engine)

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    session.add_all(instances=customers)
    session.add_all(instances=noisy_rooms)
    session.commit()
