class Employee():
    company = 'Google'
    def getSalary(self):
        print("Salary is 100k")
   


Sara = Employee()
Sara.getSalary()
# Above code is similiar to : Compiler view above as below so,there must be 1 defalt arguments in method.
Employee.getSalary('Sara')

