# Inheritance :- A way to create a new class from existing class.
# 1.Single Inheritance
class Employee:
    company = 'Google'
    def parent (self):
        print("This is a parent class.")

    def override(self):
        print("This is from Parent and not overridden.")

# Declaring a class with inheritance
class Programmers(Employee):
    language = 'Pyhton'
    def child (self):
        print("This is a child  with inheritance.")
    
    def override(self):
        print("This is from child and overrided.")

# Declaring instances of class 
obj1 = Employee()
obj2 = Programmers()

# Calling Methods and atrributes of class Employee
obj1.parent()
print(obj1.company)

# Calling Methods and attributes of class Programmers(No Inheritance)
obj2.child()
print(obj2.language)

# Calling Methods and attributes of class Programmers(with Inheritance)
obj2.parent()
print(obj2.company)

# Note :-Objects from parent can not be used by child.

# Overriding
obj1.override()
obj2.override()

