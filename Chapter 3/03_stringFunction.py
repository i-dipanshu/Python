story = "I know that you know that we all know that he know about this the whole time. "
print(story[0:6])
print(len(story)) # Counts the numbers of letters in strings
print(story.endswith("time.")) # prints true and false 
print(story.count("u")) # counts no. of occurence of the input
print(story.capitalize()) # Capatalise the first letter of the string
print(story.find("that")) # finds the input in string and prints the index of first occurence
                          # and if not found prints -1
print(story.replace("know", "Don't know")) # replaces the first input in string with second 
                                           # input in entire string.
print("This is \n an example of \t escape \\ sequence\'s characters.")