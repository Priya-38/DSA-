l = [1,2,3,4,5,6,7,8,9,99,88,77,66,55,44]
a = filter(lambda a: a%5==0, l)
print(list(a))