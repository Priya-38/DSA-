myDict = {
    "Pankha": "Fan",
    "Kitaab": "Book",
    "Ghar": "Home",
    "Chhat": "Roof"
}
print("Options are ", myDict.keys())
a=input("Enter hindi word\n")
# print("The meaning of your word is:", myDict[a])

# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:",myDict.get(a))
