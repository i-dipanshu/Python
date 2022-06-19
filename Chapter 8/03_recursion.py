# factorial of n = n * (n-1)

def factorial(n):
    if n == 1 or n == 0 :
        return 1
    else :
        return n * factorial(n-1)

num = int(input("Enter the number: "))
print(f"The factorial of {num} is {factorial(num)}.")