class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        i = 0
        for val in self.marks:
            sum += val
            i +=1
        print("hi",self.name,"your average score is ",(sum/i))
s1 = Student("Kedar Bhame",[95,95,95,95])        
s1.get_avg()
