class Person:
    country = 'India'
    
    def takeBreak(self):
        print('I am breathing...')

class Employee(Person):
    company = 'Honda'

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        print('I am an Employee and luckly i am also breathing...')

class Programmers(Employee):
    language = 'Python'

    def getSalary(self):
        print(f"No salary for Programmers.")

# Inheritance Heirrahcy    

grandParent = Person()
grandParent.takeBreak()
print(grandParent.country)

print("*************")

parent = Employee()
parent.takeBreak()
print(parent.country)
print(parent.company)

print("*************")

child = Programmers()
child.takeBreak()     # Preference is five to class it has inherited ,(parent class not grandParent)
print(child.country)
print(child.company)
print(child.language)
