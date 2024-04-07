from fastapi import APIRouter

from src.operations.noisy_rooms import read_all_noisy_rooms, read_noisy_room

router = APIRouter()


@router.get("/noisy_rooms")
def api_read_all_noisy_rooms():
    return read_all_noisy_rooms()


@router.get("/noisy_room/{noisy_room_id}")
def api_read_noisy_room(noisy_room_id: int):
    return read_noisy_room(noisy_room_id=noisy_room_id)
