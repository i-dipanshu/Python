f = open('Chapter 9\poems.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present in t")
else :
    print("Twinkle isn't present in t")
f.close()