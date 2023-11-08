# boolean withdraw(double amount)
# boolean isAccepted(double amount)


from abc import ABC, abstractmethod


class Withdraw(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def is_accepted(self, amount):
        pass
