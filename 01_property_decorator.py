class Employee:
    company = "Bharat gas"
    salary = 5600
    salarybonus = 6100
    toatalSalary = 6100

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary  

e = Employee()
print(e.totalSalary)    
e.totalSalary = 57900
print(e.salary) 
print(e.salarybonus)   