# Problem 1
myDict = {
    "Pankha": "Fan",
    "Vastu" : "Item",
    "Dabba" : "Box"
}
print("Option are ", list(myDict.keys()))
a = input("Enter the Hindi Word:  ")
# print("The meaning of Word", a, "is", myDict[a]) # throws Error when word not present
print("The meaning of Word", a, "is", myDict.get(a)) # doesn't throws Error when word not present

# Problem 2
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))
num4 = int(input("Enter Number 4: "))
num5 = int(input("Enter Number 5: "))
num6 = int(input("Enter Number 6: "))
num7 = int(input("Enter Number 7: "))
num8 = int(input("Enter Number 8: "))
s = {num1, num2, num3, num4, num5, num6, num7, num8}
print(s)

# Problem 3
s = {18, "18"}
print(s)

 # Problem 4
from re import A


s = set({})
s.add(20)
s.add(20.0) # Different Datatypes int and float but same value. so, ignored as repetition
s.add("20")
print(len(s))
print(s)

#Problem 6
favLang = {}
a = input("Enter your Favorite Language Shubham: ")
b = input("Enter your Favorite Language Ankita: ")
c = input("Enter your Favorite Language Rahul: ")
d = input("Enter your Favorite Language Sanjay: ")
e = input("Enter your Favorite Language Harshitb: ")
favLang["Shubham"] = a
favLang["Ankita"] = b
favLang["Rahul"] = c
favLang["Sanjay"] = d
favLang["Harshita"] = e
print(favLang)
