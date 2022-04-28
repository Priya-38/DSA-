import pandas as pd

pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

priyasApplication = RailwayForm()
priyasApplication.name = "Priya"
priyasApplication.train = "Prayagraj"
priyasApplication.printData()       