from dataclasses import dataclass
from datetime import datetime


@dataclass
class Customer:
    id: int
    first_name: str
    last_name: str
    email_adress: str


@dataclass
class NoisyRoom:
    id: int
    number: str
    size: int
    price: int


@dataclass
class Reservation:
    id: int
    from_time: datetime
    to_time: datetime
    customer: Customer
    room: NoisyRoom
    price: int
