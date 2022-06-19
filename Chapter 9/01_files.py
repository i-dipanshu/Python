# f = open('E:\CODES\Python\Chapter 9\sample.txt', 'r')
f = open('Chapter 9\sample.txt', 'r') # Default mode is r (read) we can skip on r
# data = f.read()   # Reads complete file
# data = f.read(5)  # reads till arument no. of letters , once we read we can't read again, so omit first line
data = f.readline() # Reads first line
print(data)
data = f.readline() # reads second line
print(data)  
f.close()
