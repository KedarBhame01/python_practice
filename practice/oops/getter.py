class Student:
    def __init__(self,name):
        self.__name = name
    
    @property
    def name(self):         #getter
        return self.__name
    
    @name.setter
    def name(self,value):         #setter
        self.__name = value
        
s1 = Student("Kedar")
print(s1.name)
s1.name = "Avishkar"
print(s1.name)

