# salary: int = input("Enter your monthly salary: ")
# tax_rate: int = input("Enter tax rate: ")

class Emp:
    def __init__(self):
        pass

    def perform_calc(self, salary, tax_rate):
        self.salary = salary
        self.tax_rate = tax_rate

        # self.mon_tax = (self.salary * self.tax_rate)/100  # formula 1
        self.mon_tax = self.salary * (self.tax_rate/100)    # formula 2
        self.mon_income = (self.salary - self.mon_tax)
        self.year_salary = (self.salary *12)
        self.year_tax = (self.mon_tax *12)
        self.year_income = (self.mon_income * 12)
        self.print_calc()
    
    def print_calc(self):
        print("------------------------------")
        print(f"Monthly income: {self.salary}")
        print(f"Tax rate: {self.tax_rate}%")
        print(f"Monthly tax: {self.mon_tax}")
        print(f"Monthly net income: {self.mon_income}")
        print(f"Yearly salary: {self.year_salary}")
        print(f"Yearly tax paid: {self.year_tax}")
        print(f"Yearly net income: {self.year_income}")
        print("------------------------------")

e1 = Emp()
e1.perform_calc(int(input("Enter your monthly salary: ")),int(input("Enter tax rate: ")))