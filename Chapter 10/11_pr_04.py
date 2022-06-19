class Calculator:
    # Declaring a constructor to take number as args.
    def __init__(self,number):
        self.number = number
    
    # Declaring a method to cube a number.
    def cube(self):
        cube = self.number**3
        print(f"The Cube of Number {self.number} is {cube}.")

    # Declaring a method to square a number.

    def square(self):
        square = self.number**2
        print(f"The square of Number {self.number} is {square}.")

    def squareRoot(self):
        squareRoot = self.number**0.5
        print(f"The squareRoot of Number {self.number} is {squareRoot}.")

class Messege:
    @staticmethod
    def greet():
        print("Hello, We welcome you to use our calculator.\nHave a great time.")

# Declaring instance of class Messege
messege = Messege()
# Method Call
messege.greet()

# Code for taking input
n = int(input("Enter a number: "))

# Declaring instance of class Calculator
num = Calculator(n)
# Method Calls
num.cube()
num.square()
num.squareRoot()
