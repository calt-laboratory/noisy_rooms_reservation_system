from src.database.models import DBNoisician, DBNoisyRoom

customers = [
    DBNoisician(first_name="Grace", last_name="Hopper", email_address="gradce_hopper@proton.me"),
    DBNoisician(first_name="Barbara", last_name="Liskov", email_address="barbara_liskov@web.de"),
    DBNoisician(first_name="Lynn", last_name="Conway", email_address="lynn_conway@posteo.de"),
    DBNoisician(first_name="Howard", last_name="Rosenbrock", email_address="howard_rosenbrock@posteo.de"),
    DBNoisician(first_name="Alexey", last_name="Chervonenkis", email_address="alexey_chervonenkis@gmx.de"),
]

noisy_rooms = [
    DBNoisyRoom(number="237", size="2", price=30),
    DBNoisyRoom(number="42", size="2", price=54),
    DBNoisyRoom(number="11", size="1", price=25),
    DBNoisyRoom(number="314", size="1", price=30),
    DBNoisyRoom(number="2718", size="2", price=40),
]
