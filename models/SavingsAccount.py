# SAVINGS_ACCOUNT_MAX_WITHDRAW"< 5.000.000đ"
# "save this object to DigitalBank by addAccount()"
from datetime import datetime

from actors.Account import Account
from interfaces.Withdraw import Withdraw
from interfaces.ReportService import *
from models.Transaction import Transaction


class SavingsAccount(Account, Withdraw, Report):
    SAVINGS_ACCOUNT_MAX_WITHDRAW = 5000000

    def __init__(self, account_id, account_pin, account_balance, is_premium):
        super().__init__(account_id, account_pin, account_balance, is_premium)

    def withdraw(self, amount):
        if self.is_accepted(amount) and self.accountBalance >= amount:
            self.accountBalance -= amount
            transaction = Transaction(self.accountID, amount, 'True')
            self.Transaction.append(transaction)
            return True
        else:
            transaction = Transaction(self.accountID, amount, 'False')
            self.Transaction.append(transaction)
            return False

    def is_accepted(self, amount):
        if amount % 10000 != 0:
            return False
        if amount < 50000:
            return False
        return 50000 <= amount <= self.SAVINGS_ACCOUNT_MAX_WITHDRAW

    def generate_report(self, amount, bank):
        transaction_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        atm_id = bank
        acc_number = self.accountId
        current_balance = self.accountBalance
        fee = 0
        return print(f'\n\t\t\t\t+----------+--------------------+----------+\n\
        \t\t\t\t|    Biên lai GD của tài khoản ATM   |\n\
        \t\t\t\t+----------+--------------------+----------+\n\
        \t\t\t\t| Ngày GD: {transaction_time}                           |\n\
        \t\t\t\t| ATM ID: {atm_id}                     |\n\
        \t\t\t\t| Số TK: {acc_number}                          |\n\
        \t\t\t\t| Số tiền: {amount}                        |\n\
        \t\t\t\t| Số dư: {current_balance}                        |\n\
        \t\t\t\t| Phí + VAT: {fee}                        |\n\
        \t\t\t\t+----------+--------------------+----------+')
