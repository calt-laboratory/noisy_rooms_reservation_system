from src.database.engine import DBSession
from src.database.models import DBNoisyRoom


def read_all_noisy_rooms() -> list[DBNoisyRoom]:
    """
    Queries the database for all noisy rooms.
    @return: List of noisy rooms
    """
    session = DBSession()
    noisy_rooms = session.query(DBNoisyRoom).all()
    return noisy_rooms


def read_noisy_room(noisy_room_id: int) -> DBNoisyRoom:
    """
    Queries a noisy room by its id.

    @param noisy_room_id: Id of a noisy room
    @return: Noisy room
    """
    session = DBSession()
    noisy_room = session.query().get(noisy_room_id)
    return noisy_room
