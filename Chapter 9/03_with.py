with open('E:\CODES\Python\Chapter 9\sample_write.txt', 'r') as f:
    a = f.read()
print(a)

with open('E:\CODES\Python\Chapter 9\sample_write.txt', 'w') as f:
    a = f.write("Writing from using 'with '")