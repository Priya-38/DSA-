class Employee:
    company ="Google"
    salary = 100000

priya = Employee()
riya = Employee()

# Creating instance attribute salary for both the objects
priya.salary = 500
riya.salary = 600
print(priya.salary)
print(riya.salary)

# Below line throws an error as address is not present in instance/class
print(riya.address)