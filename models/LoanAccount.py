# LOAN_ACCOUNT_WITHDRAW_FEE "0.05"
# LOAN_ACCOUNT_WITHDRAW_PREMIUM_FEE '0.01 for premium'
# LOAN_ACCOUNT_MAX_BALANCE "< 100.000.000đ"
# "this object save into Digital by addAccount()"
from datetime import datetime
from actors.Account import Account
from models.Transaction import Transaction


class LoanAccount(Account):
    LOAN_ACCOUNT_WITHDRAW_FEE = 0.05
    LOAN_ACCOUNT_WITHDRAW_PREMIUM_FEE = 0.01
    LOAN_ACCOUNT_MAX_BALANCE = 100000000

    def __init__(self, account_id, account_pin, is_premium):
        super().__init__(account_id, account_pin, account_balance=10000000, is_premium=is_premium)

    def checkFeeApply(self, amount):
        if not self.is_premium:
            return amount * self.LOAN_ACCOUNT_WITHDRAW_FEE
        else:
            return amount * self.LOAN_ACCOUNT_WITHDRAW_PREMIUM_FEE

    def is_accepted(self, amount) -> bool:
        if amount > self.LOAN_ACCOUNT_MAX_BALANCE:
            return False
        if self.accountBalance - (amount + self.checkFeeApply(amount)) < 50000:
            return False
        return True

    def withdraw(self, amount):
        if self.is_accepted(amount):
            self.accountBalance -= amount + self.checkFeeApply(amount)
            transaction = Transaction(self.accountID, amount, 'True')
            self.transactionID.append(transaction)
            return True
        else:
            transaction = Transaction(self.accountID, amount, 'False')
            self.Transaction.append(transaction)
            return False

    def generate_log(self, amount, bank):
        transaction_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        atm_id = bank
        acc_number = self.accountID
        current_balance = self.accountBalance
        fee = self.checkFeeApply(amount)
        return print(f'\n\t\t\t\t+----------+--------------------+----------+\n\
\t\t\t\t|    Biên lai GD của tài khoản Credit   |\n\
\t\t\t\t+----------+--------------------+----------+\n\
\t\t\t\t| Ngày GD: {transaction_time}                           |\n\
\t\t\t\t| ATM ID: {atm_id}                     |\n\
\t\t\t\t| Số TK: {acc_number}                          |\n\
\t\t\t\t| Số tiền: {amount}                        |\n\
\t\t\t\t| Số dư: {current_balance}                        |\n\
\t\t\t\t| Phí + VAT: {fee}                        |\n\
\t\t\t\t+----------+--------------------+----------+')
