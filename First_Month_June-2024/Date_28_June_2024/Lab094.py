# Test Login page

class LoginPage:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def test_login(self):
        if self.password == "pass123":
            print(f'Login of {self.username} is successful')
        else:
            print(f'Invalid password of {self.username}')


Vijay = LoginPage("Vijay@gmail.com", "123")
Ganta = LoginPage("Ganta@gmail.com", "pass123")

Vijay.test_login()
Ganta.test_login()
