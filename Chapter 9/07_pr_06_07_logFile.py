with open('Chapter 9\log.txt','r') as f:
    content = f.read()

if "python" in content.lower() :
    print("python is present")
else :
    print("No, python isn't present")

