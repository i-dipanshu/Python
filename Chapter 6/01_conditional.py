# If Else Ladder 
s = int(input("Enter Your Number: "))

if (s == 0):
    print("The No. is equal to Zero")
elif (s > 0):                            #else if is written as elif
    print("The No. is greter than Zero ")
else:
    print('The No. is non Positive.')

# Multiple If Statements
if (s == 10):
    print("The No. is equal to Ten") # All Runs independent to Each other.
if (s == 20):
    print("The No. is equal to Twenty")
if (s == 40):
    print("The No. is equal to Forty")

# Nested If
a = 45
if (s == 0):
    if(a % 5 == 0):
        print("The No. is equal to Zero")


