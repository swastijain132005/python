class student:
    #constructor
    def __init__(self,f,m):
        self.f=f
        self.m=m
        print("constructor called")
        #default constructor
    
    def hello (self):
        print("hello",self.f)

        @staticmethod
        def add(a,b):
         return a+b

s1=student("swasti","maths")
print(s1.f)