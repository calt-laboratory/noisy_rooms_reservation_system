from fastapi import FastAPI

from src.database.engine import initialize_database
from src.routers import noisy_rooms
import uvicorn

DB_FILE = "sqlite:///noisy_rooms.db"

app = FastAPI()


@app.on_event("startup")
def startup() -> None:
    """Initializes the database automatically when the API server is launched."""
    initialize_database(file=DB_FILE)


@app.get("/")
def read_root() -> str:
    return "The server is running!"


app.include_router(noisy_rooms.router)


def main() -> None:
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
