# Use open function to read the content of a file !
# f = open('sample.txt', 'r')

f = open('sample.txt', 'r') # by default the mode is r
#data = f.read()
data = f.read(4) # Read first 4 characters fromthe file 
print(data)
f.close()