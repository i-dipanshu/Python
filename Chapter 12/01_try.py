while(True):
    print("Press q to quit")
    a = input("Enter a no.: ")
    if a == "q":
        break
    try:
        a = int(a)
        if a > 6:
            print("you entered a no. a greater than 6")
    except Exception as e:
        print(f"Your input resulted in an error:{e}")
    
print("Thanks for palying a game.")