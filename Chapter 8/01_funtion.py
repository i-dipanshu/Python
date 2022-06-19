# marks = [23, 43, 56, 76, 89]
# percentage  = (sum(marks)/500)*100
# print(percentage)

def percentage(marks):
    return (sum(marks)/500)*100 # Creating a function 

a2 = [67, 78, 98, 78, 56]
percentage1 = percentage(a2)  # calling a function 
a1 = [34, 76 ,99, 78, 67]
percentage2 = percentage(a2)  # calling a function 
print(percentage1,percentage2)

def greet(name = "DefaultName"):
     print('Good Day ' + name)

greet()
greet("InputedName")