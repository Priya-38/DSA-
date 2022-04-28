class Person:
    country = "India"
    def takeBreath(self):
        print("I'm breathing....")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so I am luckily breathing....")


class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")


p = Person()
p.takeBreath()
e = Employee()
pr = Programmer()
pr.takeBreath()

