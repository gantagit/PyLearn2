#  Public, Protected, Private - Variables and Methods

class Home:

    def __init__(self, name, _email, __password):
        self.name = "Vijay"  # public variables which means anyone can access it
        self._email = "vijay.ganta@gmail.com"  # can be accessed within the in module
        # _ denotes  protected
        self.__password = "pass123"
        # can be accessed within the class
        # __ private

    def public_func(self):
        print(f'{self.name} is my name')
        print('This is Public Method')
        if self.__password == "pass123":
            print('Login Successful')
        else:
            print('Invalid Password')

        self.__change_password()

    def _protected_func(self):  # Protected method can be accessed with in the module
        print(f'{self._email} is my email')
        print('This is Protected Method')

    def __change_password_func(self):  # this is private method to change the password
        if self.__password == "pass123":
            self.__password = "ganta123"
            print(f'Password changed to {self.__password}')
        else:
            print("Invalid password")


vijay = Home("Vijay", "ganta@gmail.com", "pass12345")
vijay.public_func()
vijay._protected_func()
