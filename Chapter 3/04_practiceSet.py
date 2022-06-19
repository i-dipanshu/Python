# Problem 1
name = input("Enter your name: ")
print("Good afternoon," + name)

# Problem 2
letter = '''Dear <|Name|>,
      Greetings from lucky house, 
      you are selected!
      We welcome you with all our heart.        
Date: <|Date|> '''
name = input("Enter Your Name: ")
Date = input("Enter Date: ")
letter = letter.replace("<|Name|>", name) # Doesn't update the original list so this format (Unlike sorting in lists)
letter = letter.replace("<|Date|>", Date)
print(letter)

# Problem 3
ds = "This is a string with a  double spaces."
print(ds.find("  "))

# Problem 4
ds = ds.replace("  ", " ")
print(ds)

# Problem 5
letter = "\"Dear Rahul, \n\tThis Python course is nice!\nThanks! "
print(letter)