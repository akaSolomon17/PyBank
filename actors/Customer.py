from tabulate import tabulate

from models.SavingsAccount import *


class Customer:
    def __init__(self, customer_id, customer_name, customer_birth, customer_phone, customer_email):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_birth = customer_birth
        self.customer_phone = customer_phone
        self.customer_email = customer_email
        self.accounts = list()

    def display_information(self):
        table_info = [["ID", "Loại thẻ", "Premium", "Số dư"]]
        for account in self.accounts:
            account_type = 'SAVINGS' if isinstance(account, SavingsAccount) else 'LOAN'
            account_info = [account.accountID, account_type, account.isPremium, str(account.accountBalance)]
            table_info.append(account_info)
        colalign = ("right", "right", "right", "right")
        return tabulate(table_info, tablefmt='pretty', colalign=colalign)

    def is_AccountExist(self, account_id):
        for account in self.accounts:
            if account.accountID == account_id:
                return True
        return False

    def add_Account(self, account):
        if isinstance(account, Account):
            self.accounts.append(account)
            return True
        else:
            return False

    def get_AccountById(self, account_id):
        for account in self.accounts:
            if account.account_number == account_id:
                return account
        return False
