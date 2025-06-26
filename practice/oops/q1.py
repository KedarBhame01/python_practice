class Student:
    def __init__(self,fullname,mark_list):
            self.name = fullname
            self.marks = mark_list
    
    def average(self):
        avg = 0      
        for i in self.marks :
            avg += i
            
        print("Average of marks is :",avg / len(self.marks))
s1 = Student("Kedar",[10,20,30])
s1.average()