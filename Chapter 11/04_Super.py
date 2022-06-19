class Person:
    country = 'India'

    def __init__(self) :
        print("Intializing Grandparent...")
    
    def takeBreak(self):
        print('I am breathing...')

class Employee(Person):
    company = 'Honda'

    def __init__(self) :
        super().__init__()       # Sends the control to its superclass
        print("Intializing parent...")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        super().takeBreak()  #  Sends the control to its superclass
        print('I am an Employee and luckly i am also breathing...')

class Programmers(Employee):
    language = 'Python'
    
    def __init__(self) :
        super().__init__()     # Sends the control to its superclass
        print("Intializing child...")

    def getSalary(self):
        print(f"No salary for Programmers.")
    
    def takeBreak(self):
        super().takeBreak()   # Sends the control to its superclass
        print('I am an Programmer and  i am breathing +++')

# Inheritance Heirrahcy   

grandParent = Person()  # constructors are called upon instance creation.
grandParent.takeBreak()

print("*********")

parent = Employee()
parent.takeBreak()

print("*********")

child = Programmers()
child.takeBreak()

