class Employee:
    company = "Google"
    salary = 10000

priya = Employee()
riya = Employee()
priya.company = "Amazon"
riya.company = "Myntra"
print(priya.company)
print(riya.company)    
Employee.company = "YouTube"
print(Employee.company)
priya.salary = 2000
riya.salary = 3000
print(priya.salary)
print(riya.salary) 
