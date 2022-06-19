# Problem 1
# num = int(input("Enter the number: "))
# for i in range(1, 11):
#     # print(num, "X", i, "=", num*i)
#     print(f"{num} X {i} = {num*i}") # F strings method
#     print(reversed(f"{num} X {i} = {num*i}")) # reverse fuction.

# # Problem 2 
# l1 = ["Sohan", "Rahul", "Sachin", "Sahil", "Saurav"]
# for name in l1:
#     if name.startswith("S"):
#         print("Hello", name)

# Problem 4 
# num = int(input("Enter the number: "))
# prime = True
# for i in range(2, num):
#     if num % i == 0 :
#         prime = False
#         break
# if prime :
#     print("This number is prime")
# else:
#     print("This number is not prime")


# # Problem 6
# factorial = 1
# num = int(input("Enter the number: "))
# for i in range(1, num+1):
#     factorial *=  i
# print(f"The factorial of {num} is {factorial}")

# # Problem 8 
# n = 4
# for i in range(4):
#     print("*" * (i+1) )
 
# # Problem 7 
# n = 3
# for i in range(3):
#     print(" " * (n-i-1) +"*" * (2*i+1) +" " * (n-i-1))
#                         # We can use comma but it create a extra space.
# # Another Method
# n = int(input("Enter a number"))
# for i in range(n):
#     print(" " * (n-i-1),end = "")
#     print("*" * (2*i+1),end = "")
#     print(" " * (n-i-1))

# # Problem 9
# n = int(input("Enter a number: "))
# for i in range(n):
#     if i == 0 or i == n-1 :
#         print("*" * n)
#     else:
#         print("*" + " " * (n-2) + "*")

# # Problem 10 
# n = int(input("Enter a number: "))
# for i in range(10, 0, -1):
#     print(f"{n} X {i} = {n*i} ")

# Using While Loop 
# n = int(input("Enter a number: "))
# i = 10
# while i > 0 :
#     print(f"{n} X {i} = {n*i}")
#     i -= 1
    