from actors.Bank import *
from actors.Account import *


class DigitalBank(Bank):
    EXIT_COMMAND_CODE = 0
    EXIT_ERROR_CODE = 1

    def __init__(self, bank_name):
        super().__init__(bank_name)