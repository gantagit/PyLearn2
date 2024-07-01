#  Public, Protected, Private - Variables and Methods

class LoginPage:

    def __init__(self, name, email, password):
        self.name = name
        self.__email = email
        self.__password = password

    def login_confirm(self):
        if self.__email == "vijay.ganta@gmail.com" and self.__password == "ganta123":
            print(f'Login of {self.name} is successful')
        else:
            print(f'Login of {self.name} is unsuccessful')


vijay = LoginPage("Vijay", "test1@test.com", "vijay123")
print(vijay.name)
vijay.login_confirm()

ganta = LoginPage("Vijay Ganta", "vijay.ganta@gmail.com", "ganta123")
print(ganta.name)
ganta.login_confirm()
