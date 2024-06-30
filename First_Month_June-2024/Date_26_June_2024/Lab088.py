# Constructor example

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")


dog1 = Dog("Chow", 10)
print(dog1.name, dog1.age)  # Chow 10
dog1.bark()  # Woof!
