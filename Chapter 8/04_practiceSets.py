# # Problem 1 
# def max(num1, num2, num3):
#     if num1 > num2:
#         if num1 > num3:
#             return num1
#     else :
#         return num3
    
# num1 = int(input("Enter Number 1: "))
# num2 = int(input("Enter Number 2: "))
# num3 = int(input("Enter Number 3: "))

# print(f"The Greatest number among {num1}, {num2}, {num3} is {max(num1, num2, num3)}.")

# # Problem 2
# def farh(cel):
#     return (cel*(9/5)) + 32

# c = float(input("Enter celsius in degree: "))
# print(farh(c))

# # Problem 3
# print("Hello, " ,end = "")
# print("How ",end = "")
# print("are ",end = "")
# print("You")

# # Problem 4
# def mySum(n):
#     if n == 1 :
#         return 1
#     elif n == 0 :
#         return 0
#     else :
#         return n + mySum(n-1)

# firstSum = mySum(7)
# print(firstSum)

# Problem 5
def pattern(n):
    for i in range(n , 0, -1):
        print("*" * i)

star = int(input("Enter a number: "))
pattern(star)