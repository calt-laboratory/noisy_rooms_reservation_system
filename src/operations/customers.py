from src.database.engine import DBSession
from src.database.models import DBCustomer


def read_all_customers() -> list[DBCustomer]:
    """
    Queries the database for all customers.
    @return: List of customers
    """
    session = DBSession()
    customers = session.query(DBCustomer).all()
    session.close()
    return customers


def read_customer(customer_id: int) -> DBCustomer:
    """
    Queries a customer by its id.

    @param customer_id: Id of a noisy room
    @return: Customer
    """
    session = DBSession()
    customer = session.query(DBCustomer).get(customer_id)
    session.close()
    return customer
