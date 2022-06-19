class Employee:
    company = 'Visa'

class FreeLancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level += 1

class Programmers(Employee, FreeLancer):
    name = 'Rohit'
    
p = Programmers()
print(p.level)
print("*********")
p.upgradeLevel()
print(p.level)
print(p.company) # In case of same attributes , it prefers the first class in argument.




