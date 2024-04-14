from fastapi import APIRouter

from src.database.database_interface import DataBaseInterface
from src.database.models import DBBooking, DBNoisyRoom
from src.operations.bookings import BookingCreateData, create_booking, delete_booking, read_all_bookings, read_booking

router = APIRouter()


@router.get("/bookings")
def api_read_all_bookings():
    booking_interface = DataBaseInterface(db_class=DBBooking)
    return read_all_bookings(booking_interface=booking_interface)


@router.get("/booking/{booking_id}")
def api_read_booking(booking_id: int):
    booking_interface = DataBaseInterface(db_class=DBBooking)
    return read_booking(booking_id=booking_id, booking_interface=booking_interface)


@router.post("/booking")
def api_create_booking(booking: BookingCreateData):
    booking_interface = DataBaseInterface(db_class=DBBooking)
    room_interface = DataBaseInterface(db_class=DBNoisyRoom)
    return create_booking(data=booking, booking_interface=booking_interface, room_interface=room_interface)


@router.delete("/booking/{booking_id}")
def api_delete_booking(booking_id: int):
    booking_interface = DataBaseInterface(db_class=DBBooking)
    return delete_booking(booking_id=booking_id, booking_interface=booking_interface)
