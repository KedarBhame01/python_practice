class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
        print(self.real,"i +",self.img,"j")
    # def showNumber(self):
        
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
num1 = Complex(1,3)
# num1.showNumber()

num2 = Complex(4,6)
# num2.showNumber()

# num3 = num1.add(num2)
num3 = num1 + num2
# num3.showNumber()
