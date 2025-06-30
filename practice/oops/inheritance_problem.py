class Parent():
    def p_info(self):
        print("Parent info ---------------")
        
class Child1(Parent):
    def c1_info(self):
        print("Child1 info ---------------")
        
class Child2(Parent):
    def __init__(self,Child1_service):
        self.Child1_services = Child1_service #composition
    def show_Child1_method(self):
        self.Child1_services.c1_info()
    def c2_info(self):
        print("Child2 info ---------------")
    
c1 = Child1()
c2 = Child2(c1)
c2.c2_info() 
# c2.c1_info()
c2.show_Child1_method()