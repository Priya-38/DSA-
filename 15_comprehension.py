a = [4, 5, 7, 6, 8, 7, 9, 55, 77, 34, 67, 89]
# b = []
# for item in a:
#     if item%2 == 0:
#         b.append(item)

# print(b) 


# Shortcuts to write the same:
b = [i for i in a if i%2==0]
print(b)

t = [1,3,6,8,4,6,]
s = {i for i in t}
print(s)