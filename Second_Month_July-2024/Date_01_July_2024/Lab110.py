# Abstraction
from abc import ABC, abstractmethod


class Father(ABC):

    @abstractmethod
    def loan(self):
        pass

    def loan_cleared_status(self):
        print("Loan cleared")


class Son1(Father):

    def loan(self):
        print("son1 loan")

    # pass

    def loan_cleared_status(self):
        print("Loan cleared")


class Son2(Father):
    def loan(self):
        print("son2 loan")


s1 = Son1()
s1.loan()
S2 = Son2()
S2.loan()
