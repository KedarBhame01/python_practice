class Person:
    name = "anonymous"
    # def __init__(self,name):
    #     self.name = name
        # self.a(name)
    # cls.name = name
    
    @classmethod
    def change_name(cls,name):
        cls.name = name
        

p1 = Person()
print(p1.name)
print(Person.name)
p1.change_name("kedar")
print(p1.name)
print(Person.name)
