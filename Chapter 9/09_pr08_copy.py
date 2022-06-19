with open('Chapter 9\log.txt') as f:
    content = f.read()
with open('Chapter 9\copyLog.txt', "w") as f:
    f.write(content)