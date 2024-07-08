# Custom Exception Example

class MyExcept(Exception):

    def __init__(self, msg):
        self.message = msg
        super().__init__(msg + "\tCustom Exception")


balance = 100
withdraw = int(input("Enter amount to withdraw: "))

if withdraw > balance:
    raise MyExcept("Insufficient Balance")
else:
    balance -= withdraw
    print("Remaining Balance: ", balance)
