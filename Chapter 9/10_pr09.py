file1 = 'Chapter 9\poems.txt'
file2 = 'Chapter 9\sensor.txt'

with open('Chapter 9\poems.txt') as f:
    f1 = f.read()

with open('Chapter 9\sensor.txt') as f:
    f2 = f.read()

if f1 == f2 :
    print("Files are identical")
else :
    print("Files are not identical")