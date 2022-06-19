class Number:

    def __init__(self,num1):
        self.n = num1

    def __mul__(self,num2):
        print("Lets multiply!")
        return self.n * num2.n

    def __add__(self,num2):
        print("Lets add!")
        return self.n + num2.n
        
n1 = Number(4)
n2 = Number(5)
sum = n1 + n2
print(sum)
mul = n1 * n2
print(mul)
