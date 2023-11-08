from actors.Customer import Customer
from interfaces.Withdraw import Withdraw


class DigitalCustomer(Customer):
    def __init__(self, customer_id, customer_name, customer_birth, customer_phone, customer_email):
        super().__init__(customer_id, customer_name, customer_birth, customer_phone, customer_email)

