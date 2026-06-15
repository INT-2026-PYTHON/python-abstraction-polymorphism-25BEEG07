class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):

    def speak(self):
        print(f"{self.name} says Woof")

class Cat(Animal):

    def speak(self):
        print(f"{self.name} says Meow")

class Cow(Animal):

    def speak(self):
        print(f"{self.name} says Moo")

animals = [
    Dog("Buddy"),
    Cat("Whiskers"),
    Cow("Bessie")
]
for animal in animals:
    animal.speak()