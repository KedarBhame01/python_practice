class Frame:
    def __init__(self,height):
        self.height = height
        print("height = ",height)
    @staticmethod
    def weight():
        print("100kg is weight of frame.")
class Car(Frame):
    @staticmethod
    def start():
        print("car is stated.") 
    @staticmethod 
    def stop():
        print("car stopped.")
        
class ToyotaCar(Car):
    def __init__(self,brand,height):
        super().__init__(height)
        self.brand = brand
        
class Fortuner(ToyotaCar):
    def __init__(self,type,brand,height):
        super().__init__(brand,height)
        self.type = type
        
car1 = Fortuner("diesel","toyota","50mter")
car1.start()
print("car1.type = ",car1.type)
# print("car1.brand = ",car1.brand)
# car1.weight()
car1.stop()
