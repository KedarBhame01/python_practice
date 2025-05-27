class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
    
    @property   
    def percent(self):
        return str((self.phy + self.chem + self.math)/3) +"%"
    
stu1 = Student(92,91,93)    
print(stu1.percent)
stu1.phy = 61
print(stu1.percent)