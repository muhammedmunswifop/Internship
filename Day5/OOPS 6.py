"""6. Animal Sound System
"""

class Animal:
    def make_sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def make_sound(self):
        print("Dog: Bark")


class Cat(Animal):
    def make_sound(self):
        print("Cat: Meow")


class Cow(Animal):
    def make_sound(self):
        print("Cow: Moo")


animal1=Dog()
animal2=Cat()
animal3=Cow()

animal1.make_sound()
animal2.make_sound()
animal3.make_sound()