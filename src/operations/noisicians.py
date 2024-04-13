from pydantic import BaseModel

from src.database.engine import DBSession
from src.database.models import DBNoisician, convert_to_dict


class NoisicianCreateData(BaseModel):
    first_name: str
    last_name: str
    email_address: str


def read_all_noisicians() -> list[DBNoisician]:
    """
    Queries the database for all noisicians.
    @return: List of noisicians
    """
    session = DBSession()
    noisicians = session.query(DBNoisician).all()
    session.close()
    return [convert_to_dict(n) for n in noisicians]


def read_noisician(noisician_id: int) -> DBNoisician:
    """
    Queries a noisician by its id.

    @param noisician_id: Id of a noisician
    @return: Noisician
    """
    session = DBSession()
    noisician = session.query(DBNoisician).get(noisician_id)
    session.close()
    return convert_to_dict(obj=noisician)


def create_nosician(data: NoisicianCreateData):
    session = DBSession()
    noisician = DBNoisician(**data.dict())
    session.add(noisician)
    session.commit()
    return convert_to_dict(noisician)
