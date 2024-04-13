from fastapi import APIRouter

from src.operations.noisicians import (
    NoisicianCreateData,
    NoisicianUpdateData,
    create_nosician,
    read_all_noisicians,
    read_noisician,
    update_noisician,
)

router = APIRouter()


@router.get("/noisicians")
def api_read_all_noisicians():
    return read_all_noisicians()


@router.get("/noisician/{noisician_id}")
def api_read_noisician(noisician_id: int):
    return read_noisician(noisician_id=noisician_id)


@router.post("/noisician")
def api_create_noisician(noisician: NoisicianCreateData):
    return create_nosician(data=noisician)


@router.post("/noisician/{noisician_id}")
def api_update_noisician(noisician_id: int, data: NoisicianUpdateData):
    return update_noisician(noisician_id=noisician_id, data=data)
