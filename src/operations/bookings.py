from datetime import date

from pydantic import BaseModel

from src.operations.interface import DataInterface, DataObject


class BookingCreateData(BaseModel):
    noisy_room_id: int
    noisician_id: int
    from_date: date
    to_date: date


def read_all_bookings(booking_interface: DataInterface) -> list[DataObject]:
    return booking_interface.read_all()


def read_booking(booking_id: int, booking_interface: DataInterface) -> DataObject:
    return booking_interface.read_by_id(id=booking_id)


def create_booking(
        data: BookingCreateData,
        booking_interface: DataInterface,
        room_interface: DataInterface,
) -> DataObject:
    noisy_room = room_interface.read_by_id(data.noisy_room_id)
    booking_duration_in_days = (data.to_date - data.from_date).days
    if booking_duration_in_days <= 0:
        raise ValueError("Booking time must be greater than 0")
    booking_dict = data.dict()
    booking_dict["price"] = noisy_room["price"] * booking_duration_in_days
    return booking_interface.create(booking_dict)


def delete_booking(booking_id: int, booking_interface: DataInterface) -> DataObject:
    return booking_interface.delete(id=booking_id)
