from fastapi import FastAPI

from src.hotel.database.engine import initialize_database, DBSession
from src.hotel.database.models import DBNoisyRoom

DB_FILE = "sqlite:///noisy_rooms.db"

app = FastAPI()


@app.on_event("startup")
def startup() -> None:
    """Initializes the database automatically when the API server is launched."""
    initialize_database(file=DB_FILE)


@app.get("/")
def read_root() -> str:
    return "The server is running!"


@app.get("/noisy_room")
def read_all_noisy_rooms():
    session = DBSession()
    noisy_rooms = session.query(DBNoisyRoom).all()
    return noisy_rooms
