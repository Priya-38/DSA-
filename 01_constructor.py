class Employee():
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = 50000
        self.subunit = subunit
        print("Employee is created!")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"the salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")  

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod   
    def greet():
        print("Good Morning, Priya")

    @staticmethod
    def time():
        print("The time in this morning is 10PM")

priya = Employee("priya", 5000, "YouTube")
#priya = Employee()   --> This throws an error (missing 3 required positional arguments:)    
priya.getDetails()
        