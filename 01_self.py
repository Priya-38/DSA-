class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.Salary}")

priya = Employee()
#print(priya.company)
priya.Salary = 500000000
priya.getSalary()       # Employee.getSalary(priya)        