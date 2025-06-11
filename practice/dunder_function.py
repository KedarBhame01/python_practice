class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def showcomplex(self):
        print(self.real,"i +",self.img,"j")
        # __add__ is a dunder function
        # not because we user __ before and after
        # is a specific name of __add__
    def __add__(self,num2):     
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal, newimg)

com1 = Complex(1,3)
com1.showcomplex()

com2 = Complex(3,5)
com2.showcomplex()

com3 = com1 + com2
# com3 =com1.add(com2)
com3.showcomplex()
