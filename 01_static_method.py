class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.Salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good morning, Sir")
    
    @staticmethod
    def time():
        print("the time is 9AM in this morning")    


priya = Employee()
#print(priya.company)
priya.Salary = 500000000
priya.getSalary("Thanks")       # Employee.getSalary(priya) 
priya.greet()  # Employee.greet()  
priya.time()     