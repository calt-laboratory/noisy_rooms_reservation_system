from datetime import datetime

from src.database.engine import DBSession
from src.database.models import DBBooking, convert_to_dict
from pydantic import BaseModel


class BookingCreateData(BaseModel):
    noisy_room_id: int
    noisician_id: int
    from_time: datetime
    to_time: datetime


def read_all_bookings():
    session = DBSession()
    bookings: list[DBBooking] = session.query(DBBooking).all()
    session.close()
    return [convert_to_dict(booking) for booking in bookings]


def read_booking(booking_id: int):
    session = DBSession()
    booking_id = session.query(DBBooking).get(booking_id)
    session.close()
    return convert_to_dict(booking_id)


def create_booking(data: BookingCreateData):
    session = DBSession()

    # Get noisy room information by noisy room id
    noisy_room = session.query(DBBooking).get(data.noisy_room_id)

    booking_time = data.to_time - data.from_time
    print("##############################################################")
    print(f"Booking time: {booking_time}")
    if booking_time <= 0:
        raise ValueError("Booking time must be greater than 0")

    booking_dict = data.dict()
    booking_dict["price"] = noisy_room.price * booking_time

    booking = DBBooking(**data.dict())
    session.add(booking)
    session.commit()
    return convert_to_dict(booking)


def delete_booking(booking_id: int):
    session = DBSession()
    booking = session.query(DBBooking).get(booking_id)
    session.delete(booking)
    session.commit()
    return convert_to_dict(booking)
