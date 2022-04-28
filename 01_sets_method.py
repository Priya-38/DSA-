# Creating an empty set
a = set()
print(type(a)) 

## Adding values to an empty set 
a.add(5)
a.add(6)
a.add(6) # adding value repeatedly does not change a set
a.add(4)
a.add(3)
a.add((3,5,4,6))

## Accessing Elements
# a.add({4:5}) # Cannot add list or dictionary to sets
print(a)

## Length of the set
print(len(a)) # Prints the length of the set

## Removal of an item
a.remove(6) # Remove 6 from the set a
#a.remove(20) # Throws an error while trying to remove 20 (which is not present in the set)
print(a) 

print(a.pop())
print(a)

a.clear()
print(a)