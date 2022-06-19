myDict = {
    "Fast" : "In a Quick manner" ,
    "Ramcharan" : "Noun, a name",
    'Marks' : [1, 2, 5],
    'anotherDict': {"You": "A Pronoun"} #Nested Dictionary
}
print(myDict["Fast"])
print(myDict["Ramcharan"])
print(myDict["Marks"])
print(myDict["anotherDict"])
print(myDict["anotherDict"]["You"])
myDict["Marks"] = [43, 42, 41, 45] # We can change the value of elements in Dictionary.
print(myDict['Marks'])
