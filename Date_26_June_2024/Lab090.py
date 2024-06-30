# Constructor example

class Dog:
    name = None
    age = None

    def __init__(self):
        print("Default Constructor with No Arguments")

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def bark(self):
        print(f'Dog {self.name} of age {self.age} is barking "Woof!"')


dog1 = Dog("Chow", 10)
dog2 = Dog("Puppy", 5)
dog3 = Dog()  # Default Constructor with No Arguments
print(dog1.name, dog1.age)  # Chow 10
print(dog2.name, dog2.age)  # Puppy 5

dog1.bark()
dog2.bark()
dog3.bark()
