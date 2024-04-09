from src.database.engine import DBSession
from src.database.models import DBNoisician


def read_all_noisicians() -> list[DBNoisician]:
    """
    Queries the database for all noisicians.
    @return: List of noisicians
    """
    session = DBSession()
    noisicians = session.query(DBNoisician).all()
    session.close()
    return noisicians


def read_noisician(noisician_id: int) -> DBNoisician:
    """
    Queries a noisician by its id.

    @param noisician_id: Id of a noisician
    @return: Noisician
    """
    session = DBSession()
    noisician = session.query(DBNoisician).get(noisician_id)
    session.close()
    return noisician
