from hashlib import md5


myDict = {
#    Key   :  Values
    "fast" : "In a Quick manner" ,
    "ramcharan" : "Noun, a name",
    'marks' : [1, 2, 5],
    'anotherDict': {"You": "A Pronoun"} #Nested Dictionary
}
print(list(myDict.keys())) # Prints the keys of Dict, Default type DictKeys
print(list(myDict.values())) #Prints the Values of Dict, Default type DictKeys
print(myDict.items()) # Prints the keys, Value of the contents of Dict
print(myDict)
update_Dict = {
    "Love" : "A Verb",
    'Hate' : "A verb",
    'Care' : "Another Verb",
    'marks': [2.3, 45.5, "Ram"]
}
myDict.update(update_Dict) # Updates the values of Dict 
print(myDict)
print(myDict.get("Harry")) # Throws None as Harry is not Present in Dictionary
# print(myDict["Harry"])  # Throws Error as Harry is not Present in Dictionary
print(myDict.get("ramcharan"))
print(myDict["ramcharan"])
