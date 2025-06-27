class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math)/3)
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)

stu1 = Student(10,20,30)
print(stu1.percentage)
stu1.phy = 50
print(stu1.percentage)