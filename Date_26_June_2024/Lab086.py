# Class example

class Person:
    # Attributes # Properties # Data Members
    name = None
    age = None
    phone_number = None
    email_id = None

    # Behaviours # Methods # Member functions
    def walk(self):  # No Arguments passing and No Returns
        print("I am walking")

    def sleep(self, name):  # Arguments passing and No Returns
        print(f"{name} is walking")

    def eat(self, name):  # Arguments passing and Returns
        print(f"{name} is eating")
        return "Eating"

    def see(self):  # No Arguments passing and Returns
        return print("I am seeing")


