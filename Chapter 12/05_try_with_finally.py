try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:
    print("We were Done.") # It always get executed without giving a fuck.
print("Thanks for usnig the program.") # if exception this doesn't get printed.