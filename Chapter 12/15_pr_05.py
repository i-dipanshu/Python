num = int(input("Enter a number: "))
table = [num*i for i in range(1, 11)]
print(table)

with open("E:\CODES\Python\Chapter 12\ tables.txt", "w") as f:
    f.write(str(table))
    f.write("\n")