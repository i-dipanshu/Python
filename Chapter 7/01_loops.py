# While loop
i = 1
while i <= 50 :  # Condition is checked first and executes until it becomes False.
    print (str(i))
    i += 1
print("Done")

# For Loop
l = [1, "Aradhaya", 43.5]
for item in l :
    print(item)

# Range Function
for i in range(10): # gives 0(default) to 10-1 = 9 by step 1 (default)
    print(i)
for i in range(2,33,3): # gives 2 to 32 by step 2
    print(i)

# For with else 
for i in range(10):
    print(i)
else:
    print("This is inside of loop") # As soon as for loop succesfully terminates, else block executes

# Break statement
for i in range(9) :
    print (i)
    if i == 5 :
        break
else :
    print("Break hasn't terminated the loop")

# Continue statement
for i in range(9) :
    if i == 5 :
        continue
    print (i)
else :
    print("Break hasn't terminated the loop")

# Pass Statement 
i = {4, 5, 6, 7}
for item in i:
    pass
if i == 4 :
    pass
def func1(player1, player2):
    pass