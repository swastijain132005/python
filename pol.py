#operator overloading
print(1+2)
print("Hello"+" World")
print([1,2]+[3,4])

class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def shownum(self):
        print(self.real,"i +",self.imag,"j")
    def add(self,other):
        newr=self.real+other.real
        newi=self.imag+other.imag
        return complex(newr,newi)

    #dunder functions starts with __ and are used to override the default behaviour of the class
    def __add__(self,other):
        newr=self.real+other.real
        newi=self.imag+other.imag
        return complex(newr,newi)
    def __sub__(self,other):
        newr=self.real-other.real
        newi=self.imag-other.imag
        return complex(newr,newi)
num1=complex(1,2)
num1.shownum()
num2=complex(3,4)
num2.shownum()
num3=num1.add(num2)
num3.shownum()
num4=num1-num2
num4.shownum()
num5=num1+num2
num5.shownum()

#but we want that anyone  can do print(num1+num2) then we can use operator overloading