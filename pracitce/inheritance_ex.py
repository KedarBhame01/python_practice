class car:
    def __init__(self):
        self.acc = "12345"
        self.pwd = "password"

class fourWheelar(car):
    def __init__(self):
        super().__init__()
        self.wheels = 4
        
class fortuner(fourWheelar):
    def __init__(self, type):
        super().__init__()
        self.type = type
        self.power = "high"

c1 = fortuner("disel")
print(c1.type)
print(c1.power)
print(c1.wheels)
print(c1.acc)
print(c1.pwd)