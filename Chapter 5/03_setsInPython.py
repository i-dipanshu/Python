a = {2, 3, 4, 5, 2}
print(a) # No repetitive elements in sets , ignores the repetion
print(type(a))
#Empty Set
b = {} # create an empty dictionary
print(type(b))
b = set({})
print(type(b))
b.add(6) # adds 6 to the set
b.add(6)
print(a) # Ignores Repetion
# b.add([4, 5, 6]) # Can't add lists to sets
# b.add({4:5, 6:7}) # Can't add Dictionary to sets
b.add((9, 5, 6))  # But Tuple can be added as it is hasable
print(b)
print(len(b)) # Prints the length of set
print(len(a))
b.remove(6) # Removes 6 from set, throws an error when value not present
print(b)
print(a.pop()) # Removes a random element from the set
print(a)
b.clear() # Empty The Set
print(b)
