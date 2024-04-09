from fastapi import APIRouter

from src.operations.noisicians import read_all_noisicians, read_noisician

router = APIRouter()


@router.get("/noisicians")
def api_read_all_noisicians():
    return read_all_noisicians()


@router.get("/noisician/{noisician_id}")
def api_read_noisician(noisician_id: int):
    return read_noisician(noisician_id=noisician_id)
