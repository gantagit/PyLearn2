#  Public, Protected, Private - Variables and Methods using Bank


class BankAccount:
    balance = 0

    def __init__(self):
        print("Welcome to Bank")

    def __show_balance(self):
        print("Your balance is ", self.balance)

    def __get_withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def check_auth_for_balance(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("Authentication Failed")

    def check_auth_for_withdraw(self, auth, amount):
        if auth:
            self.__get_withdraw(amount)
        else:
            print("Authentication Failed")
