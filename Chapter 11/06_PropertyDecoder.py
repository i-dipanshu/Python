class Employee :
    company = 'Bharat gas'
    salary = 5600
    salaryBonus = 500
    # totalSolary = 6100

    @property   # it makaes method a property --- also a getter method
    def totalSalary(self):
        return self.salary + self.salaryBonus

    # @totalSalary.setter
    # def totalSalary(self, val):
    #     self.salaryBonus = val - self.salary


obj = Employee()
print(obj.totalSalary)
obj.totalSalary = 5800
print(obj.salary)
print(obj.salaryBonus)
