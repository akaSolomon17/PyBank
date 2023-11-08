from actors.Customer import Customer


class Bank:
    def __init__(self, bank_name):
        self.name = bank_name
        self.customers = list()

    def getCusById(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return False

    def addCustomer(self, customer):
        if isinstance(customer, Customer):
            self.customers.append(customer)
            return True
        else:
            return False

