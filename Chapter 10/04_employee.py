class Employee:
    # 1. Class atrributes :- Same for everyone
    company = 'Google' 
    # Instance attributes takes preference over class attributes.
    salary = 30000 
# Creatiing a object 
Sanjiv = Employee()
Hardy = Employee()
Shubham = Employee()

# 2. Instance attributes :- Belongs to instance
Sanjiv.salary = 80000
Hardy.salary = 100000

# Calling a method and printing class attributes
print(Sanjiv.company)  
print(Hardy.company)

# Changing Class Attributes
Employee.company = 'Youtube'

# Calling a method and printing class attributes
print(Sanjiv.company)  
print(Hardy.company)

# Calling a method and printing instance attributes
print(Sanjiv.salary)  
print(Hardy.salary)

# Takes Class attributes as there is no instance attributes.
print(Shubham.salary) 