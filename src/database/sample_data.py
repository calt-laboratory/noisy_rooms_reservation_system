from src.database.models import DBCustomer, DBNoisyRoom


customers = [
    DBCustomer(
        first_name="Grace",
        last_name="Hopper",
        email_adress="gradce_hopper@proton.me"
    ),
    DBCustomer(
        first_name="Barbara",
        last_name="Liskov",
        email_adress="barbara_liskov@web.de"
    ),
    DBCustomer(
        first_name="Lynn",
        last_name="Conway",
        email_adress="lynn_conway@posteo.de",
    ),
    DBCustomer(
        first_name="Howard",
        last_name="Rosenbrock",
        email_adress="howard_rosenbrock@posteo.de",
    ),
    DBCustomer(
        first_name="Alexey",
        last_name="Chervonenkis",
        email_adress="alexey_chervonenkis@gmx.de",
    ),
]

noisy_rooms = [
    DBNoisyRoom(number="237", size="2", price=30),
    DBNoisyRoom(number="42", size="2", price=54),
    DBNoisyRoom(number="11", size="1", price=25),
    DBNoisyRoom(number="314", size="1", price=30),
    DBNoisyRoom(number="2718", size="2", price=40),
]
