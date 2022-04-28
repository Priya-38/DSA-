myDict={
    "Fast": "In a quick manner",
    "Priya": "A Coder",
    "Marks": [1,2,3],
    "anotherdict": {'priya': 'student'}
}

# Dictionary Methods
print(list(myDict.keys())) # Print the keys of the dictioinary
print(myDict.values()) # Print the values of the dictionary
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary
print(myDict)
updateDict = {
    "Priya": "Good",
    "PV Sindhu": "Player",
    "Lata Mangeshkar": "Singer",
    "Mukesh Ambani": "Business"
}
myDict.update(updateDict) # Update the dictionary bt adding key-value pairs from updateDict
print(myDict)

print(myDict.get("Priya")) # Prints the value associated with the key "Priya"
print(myDict["Priya"]) # Prints value associated with key "Priya"

# The difference between .get and [] syntax in dictionaries?
print(myDict.get("Priya2")) # Returns NONE as Priya2 is not present in the dictionary
print(myDict["Priya2"]) # Throws an error as Priya2 is not present in the dictionary