import Lab086

a = Lab086.Person()  # importing the class Person from Lab086.py
b = Lab086.Person()

# Creating Object for Class
# a is reference, () is object, Person is class
a.name = "Vijay"
a.age = 30
a.phone_number = 1234567890
a.email_id = a.name + str(a.age) + "@test.com"

a.walk()
a.sleep(a.name)
a.eat(a.name)
a.see()

b.name = "Ajay"
b.age = 25
b.phone_number = 987654321
b.email_id = b.name + str(b.age) + "@test.com"

b.walk()
b.sleep(b.name)
b.eat(b.name)
b.see()
