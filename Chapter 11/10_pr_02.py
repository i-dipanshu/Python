from ast import stmt
from os import stat


class Animal:
    anmimalType = "Mammal"

class Pets(Animal):
    petType = "Cat"

class Dog(Pets) :
    @staticmethod
    def bark():
        print("Bauh Bauh")

obj = Dog()
obj.bark()