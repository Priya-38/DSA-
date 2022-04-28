#marks1 = int(input("Enter marks1: "))
#marks2 = int(input("Enter marks2: "))
#marks3 = int(input("Enter marks3: "))
#marks4 = int(input("Enter marks4: "))
#percentage = ((marks1+marks2+marks3+marks4)/400)*100
#print(percentage)

#marks5 = int(input("Enter marks5: "))
#marks6 = int(input("Enter marks6: "))
#marks7 = int(input("Enter marks7: "))
#marks8 = int(input("Enter marks8: "))
#percentage = ((marks5+marks6+marks7+marks8)/500)*100
#print(percentage)

def percent(marks):
    return ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100

marks1 = [45,56,67,55]
percentage1 = percent(marks1)

marks2 = [75, 98, 88, 78]
percentage2 = percent(marks2)
print(percentage1, percentage2)


