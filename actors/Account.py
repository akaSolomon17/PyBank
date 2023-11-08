
from interfaces.ReportService import Report
from interfaces.Withdraw import Withdraw


class Account(Withdraw, Report):

    def __init__(self, account_id, account_pin, account_balance, is_premium):
        self.accountPIN = account_pin
        self.accountID = account_id
        self.accountBalance = account_balance
        self.transactionID = list()
        self.isPremium = is_premium

    # GET
    @property
    def accountId(self):
        return self.accountID

    @property
    def aTransId(self):
        return self.transactionID

    @property
    def accountPin(self):
        return self.accountPIN

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # SET
    @accountId.setter
    def accountId(self, account_id):
        self.accountID = account_id

    @aTransId.setter
    def aTransId(self, transaction_id):
        self.transactionID = transaction_id

    @accountPin.setter
    def accountPin(self, account_pin):
        self.accountPIN = account_pin

    # def deposit(self, amount):
    #     if amount > 0:
    #         self.accountBalance += amount
    #         return True
    #     else:
    #         return False

    # PRINT
    def print_info(self):
        return print(f'\n\t\t\t\t+----------+--------------------+----------+\n\
\t\t\t\t|    Thông tin tài khoản {self.accountID}   |\n\
\t\t\t\t+----------+--------------------+----------+\n\
\t\t\t\t| PIN: {self.accountPIN}                           |\n\
\t\t\t\t| Số dư: {self.accountBalance}                     |\n\
\t\t\t\t| Loại tài khoản: {self.isPremium}                          |\n\
\t\t\t\t+----------+--------------------+----------+')

    def withdraw(self, amount):
        pass

    def generate_report(self, amount, bank):
        pass
