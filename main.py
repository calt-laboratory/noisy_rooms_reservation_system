from pathlib import Path

import uvicorn
from fastapi import FastAPI

from src.database.engine import initialize_database
from src.database.create_database import create_database
from src.routers import noisicians, noisy_rooms, bookings

DB_FILE = "sqlite:///noisy_rooms.db"

if not Path("noisy_rooms.db").exists():
    create_database(file=DB_FILE)
else:
    print(f"Database file '{Path(DB_FILE).stem}' already exists. Skipping creation.")


app = FastAPI()


@app.on_event("startup")
def startup() -> None:
    """Initializes the database automatically when the API server is launched."""
    initialize_database(file=DB_FILE)


@app.get("/")
def read_root() -> str:
    return "The server is running!"


app.include_router(noisy_rooms.router)
app.include_router(noisicians.router)
app.include_router(bookings.router)


def main() -> None:
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
