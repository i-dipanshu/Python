class Employee():
    company = 'Google'
    salary = 200000

    def getSalary(self, signature, DOB):
        print(f"Salary for this Employee working in {self.company} is {self.salary}.\n {signature}\n{DOB}")
    
    @staticmethod
    # Static Method makes function takes no self arguments
    def greet():
        print ("Good Morning, Sir")

    @staticmethod
    def time():
        print("9 am in the Morning.")

Maya = Employee()
# Declaring a instance variable
Maya.salary = 1000000 
Maya.getSalary('Thanks','27 Feb') # Employee.getSalary("Maya")
Maya.greet()     # Employee.greet() :- Static Method

