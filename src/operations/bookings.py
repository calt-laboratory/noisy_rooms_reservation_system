from datetime import date

from pydantic import BaseModel

from src.database.engine import DBSession
from src.database.models import DBBooking, DBNoisyRoom, convert_to_dict


class BookingCreateData(BaseModel):
    noisy_room_id: int
    noisician_id: int
    from_date: date
    to_date: date


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
    noisy_room = session.query(DBNoisyRoom).get(data.noisy_room_id)
    booking_duration_in_days = (data.to_date - data.from_date).days
    if booking_duration_in_days <= 0:
        raise ValueError("Booking time must be greater than 0")
    booking_dict = data.dict()
    booking_dict["price"] = noisy_room.price * booking_duration_in_days
    booking = DBBooking(**booking_dict)
    session.add(booking)
    session.commit()
    return convert_to_dict(booking)


def delete_booking(booking_id: int):
    session = DBSession()
    booking = session.query(DBBooking).get(booking_id)
    session.delete(booking)
    session.commit()
    return convert_to_dict(booking)
