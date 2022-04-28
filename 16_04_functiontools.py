from functools import reduce
l = [3,5,8,9,3,5,54,45]

a = reduce(max,l)
print(a)