import sys
import os

import keyboard

from models.DigitalBank import *
from actors.Customer import *
from models.LoanAccount import LoanAccount

banking = DigitalBank("PyBank")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def initData():
    customer1 = Customer("252112","Tran Ngo Quoc Huy", "17-01-2001", "0775596428", "quochuy.4work@gmail.com")
    customer2 = Customer("252113", "Tran Huy", "05-10-1999", "0985919210", "tranhuy123@gmail.com")
    customer3 = Customer("252119", "Bap Quoc", "20-01-1945", "0985522443", "solomon4learn@gmail.com")
    account_first = SavingsAccount(252122, "1234",  "1.000.000đ", True)
    account_second = LoanAccount(122101, "1252", False)
    account_third = SavingsAccount(252198, "1701", "1.000.000đ", False)
    account_fourth = LoanAccount(252231, "1005", True)
    customer1.add_Account(account_first)
    customer2.add_Account(account_third)
    customer3.add_Account(account_second)
    customer2.add_Account(account_fourth)
    banking.addCustomer(customer1)
    banking.addCustomer(customer2)
    banking.addCustomer(customer3)


def displayMenu():
    func = 1
    while func != 0:
        print("\t\t\t\t+----------+--------------------+----------+")
        print("\t\t\t\t|  BANK MANAGEMENT SYSTEM | PyBank@v1.0.0  |")
        print("\t\t\t\t+----------+--------------------+----------+")
        print("\t\t\t\t| 1. Thông tin khách hàng                  |")
        print("\t\t\t\t| 2. Thêm tài khoản ATM                    |")
        print("\t\t\t\t| 3. Thêm tài khoản tín dụng               |")
        print("\t\t\t\t| 4. Rút tiền                              |")
        print("\t\t\t\t| 5. Lịch sử giao dịch                     |")
        print("\t\t\t\t| 0. Thoát                                 |")
        print("\t\t\t\t+----------+--------------------+----------+")
        func = int(input("\t\t\t\tChức năng:"))
        if func == 1:
            cccd_input = input("\n\t\t\t\tNhập CCCD khách hàng bạn muốn tìm:")
            if banking.getCusById(cccd_input):
                print(banking.getCusById(cccd_input).display_information())
                if keyboard.is_pressed("enter"):
                    break
            else:
                print("Sai CCCD!")
        elif func == 2:
            cccd_input = input("\n\t\t\t\tNhập CCCD khách hàng bạn muốn tìm:")
            if banking.getCusById(cccd_input):
                info_saving = banking.getCusById(cccd_input)
            else:
                print("\n\t\t\t\tKhông tìm thấy CCCD!")
                return
            print("\n\t\t\t\t+----------+THÊM TÀI KHOẢN TIẾT KIỆM (DEBIT CARD)+----------+")
            account_id = input("\n\t\t\t\tVui lòng nhập số CCCD:")
            while len(account_id) != 6 or info_saving.is_AccountExist(account_id) or not account_id.isnumeric():
                if len(account_id) != 6 or not account_id.isnumeric():
                    print("\n\t\t\t\tVui lòng nhập đúng 12 ký tự số cho CCCD!")
                elif info_saving.is_AccountExist(account_id):
                    print("\n\t\t\t\tCCCD Đã tồn tại trong hệ thống!")
                account_id = input("\n\t\t\t\tNhập lại CCCD:")
            account_pin = input("\n\t\t\t\tVui lòng nhập mã PIN(4 ký tự số):")
            while len(account_pin) != 4 or not account_pin.isnumeric():
                if len(account_pin) != 4 or not account_pin.isnumeric():
                    print("\n\t\t\t\tVui lòng nhập đúng 4 ký tự số cho mã PIN!")
            account_balance = input("\n\t\t\t\tNhập số dư bạn muốn thêm vào tài khoản(Nhập số):")
            while not account_balance.isnumeric():
                if not account_balance.isnumeric():
                    print("\n\t\t\t\tVui lòng nhập số dư dưới 100 triệu và chỉ ký tự số!")
                    account_balance = input("\n\t\t\t\tNhập lại số dư theo đúng điều kiện:")
                else:
                    print("\n\t\t\t\tChúc mừng bạn đã tạo tài khoản và thêm số dư thành công!")

            savingAccount = SavingsAccount(account_id, account_pin, account_balance, is_premium=False)
            info_saving.add_Account(savingAccount)
        elif func == 3:
            cccd_input = input("\n\t\t\t\tVui lòng nhập CCCD:")
            if banking.getCusById(cccd_input):
                info_loan = banking.getCusById(cccd_input)
            else:
                print("\n\t\t\t\tKhông tìm thấy CCCD!")
                return

            print("\n\t\t\t\t+----------+THÊM TÀI KHOẢN TIẾT KIỆM (DEBIT CARD)+----------+")

            account_id = input("\n\t\t\t\tVui lòng nhập số CCCD:")
            while len(account_id) != 6 or info_loan.is_AccountExist(account_id) or not account_id.isnumeric():
                if len(account_id) != 6 or not account_id.isnumeric():
                    print("\n\t\t\t\tVui lòng nhập đúng 12 ký tự số cho CCCD!")
                elif info_loan.is_AccountExist(account_id):
                    print("\n\t\t\t\tCCCD Đã tồn tại trong hệ thống!")
                account_id = input("\n\t\t\t\tNhập lại CCCD:")
            account_pin = input("\n\t\t\t\tVui lòng nhập mã PIN(4 ký tự số):")
            while len(account_pin) != 4 or not account_pin.isnumeric():
                if len(account_pin) != 4 or not account_pin.isnumeric():
                    print("\n\t\t\t\tVui lòng nhập đúng 4 ký tự số cho mã PIN!")
            loanAccount = LoanAccount(account_id, account_pin, is_premium=False)
            info_loan.add_Account(loanAccount)
        elif func == 4:
            cccd_input = input("\n\t\t\t\tNhập CCCD của bạn:")
            if banking.getCusById(cccd_input):
                cus_info = banking.getCusById(cccd_input)
            else:
                print("\n\t\t\t\tKhông tìm thấy CCCD!")
                return
            id_input = input("\n\t\t\t\tNhập số tài khoản:")
            if cus_info.get_AccountById(id_input):
                acc_info = cus_info.get_AccountById(id_input)
            else:
                print("\n\t\t\t\tKhông tìm thấy tài khoản!")
                return
            acc_pin = input("\n\t\t\t\tNhập PIN tài khoản:")
            if acc_info.account_pin != acc_pin:
                print("\n\t\t\t\tSai mã PIN!")
                return
            withdraw_amount = print("\n\t\t\t\tNhập số tiền muốn rút:")
            if not withdraw_amount.isnumeric():
                print("\n\t\t\t\tVui lòng chỉ nhập số!")
            if acc_info.withdraw(withdraw_amount):
                print("\n\t\t\t\tRút tiền thành công!")
                acc_info.log(withdraw_amount,banking.name)
            else:
                print("\n\t\t\t\tRút tiền thất bại!")

        elif func == 5:
            cccd_input = input("\n\t\t\t\tNhập CCCD:")
            if banking.getCusById(cccd_input):
                cus_info = banking.getCusById(cccd_input)
            else:
                print("\n\t\t\t\tKhông tìm thấy CCCD!")
                return
            id_input = input("\n\t\t\t\tNhập số tài khoản:")
            if cus_info.get_AccountById(id_input):
                acc_info = cus_info.get_AccountById(id_input)
            else:
                print("\n\t\t\t\tKhông tìm thấy tài khoản!")
                return
            acc_pin = input("\n\t\t\t\tNhập PIN tài khoản:")
            if acc_info.account_pin != acc_pin:
                print("\n\t\t\t\tSai mã PIN!")
                return
            print(acc_info.displayTransactions())
        else:
            sys.exit()
        clear_console()


if __name__ == "__main__":
    initData()
    displayMenu()
