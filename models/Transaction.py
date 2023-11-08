# id String (tao ma random)
# accountNumber String "Ma TK cua KH, Chi tra ve khi KH co CCCD trong bank neu khong thi tra ve NULL"
# amount double "So tien ma KH muon rut"
# time String "thoi diem giao dich Date()"
# status Boolean "True la giao dich thanh cong, nguoc lai False"
# "Lưu danh sách gd trong mỗi loại acc. Rút tiền thì lưu lại lịch sử"
# "Thông tin giao dịch: info Khách Hàng - info GD"


from datetime import datetime
import random


class Transaction:
    def __init__(self, account_id, amount, status):
        self.atmId = random.randint(100, 999)
        self.dateTime = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.accountId = account_id
        self.amount = amount
        self.status = status
