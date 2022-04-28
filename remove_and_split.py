def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this =  "     Priya is a good girl     "
n= remove_and_split(this, "Priya") 
print(n)
print(this)
print(this.strip())