class Employee():
    company = 'Google'
    salary = 200000

    # def __init__(self):       # At a time only one constructors can be created.
    #     print("I am Constructor, runs on object instantiation.")

    def __init__(self, name, salary, subunit):
        print(f"Name = {name} \nSalary = {salary} \nSubunit = {subunit}")

    def __init2__(self):
        print("I am not a Constructor, and doesn't runs on object instantiation, and runs on method call only.")

    def getSalary(self, signature, DOB):
        print(f"Salary for this Employee working in {self.company} is {self.salary}.\n {signature}\n{DOB}")

# # As soon as object is intantiated , constructor is called.    
# obj1 = Employee()    
# # Runs Only on Method Call
# obj1.__init2__()
obj2 = Employee("Maya", '500000', 'Railway')
