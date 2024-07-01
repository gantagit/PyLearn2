#  Public, Protected, Private - Variables and Methods using Bank

from Lab098 import BankAccount

jp_chase = BankAccount()


def show_balance():
    secret_pin = int(input("Enter your pin to see balance: "))
    if secret_pin == 1234:
        jp_chase.check_auth_for_balance(True)
    else:
        jp_chase.check_auth_for_balance(False)


def withdraw_amount():
    secret_pin = int(input("Enter your pin to withdraw amount: "))
    amount_to_withdraw = int(input("Enter amount to withdraw: "))
    if secret_pin == 1234:
        jp_chase.check_auth_for_withdraw(True, amount_to_withdraw)
    else:
        jp_chase.check_auth_for_withdraw(False, amount_to_withdraw)


jp_chase.deposit(101)
show_balance()
jp_chase.deposit(200)
withdraw_amount()
jp_chase.deposit(300)
show_balance()
