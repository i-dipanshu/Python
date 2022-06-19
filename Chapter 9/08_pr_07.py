content = True
i = 1
with open('Chapter 9\log.txt') as f:
    while content :
        content = f.readline()
        if 'python' in content.lower():
            print("Yes, Python is present in log data on line no.",i)
            print(content)
        i += 1