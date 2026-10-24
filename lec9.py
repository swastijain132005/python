class student:
    def __init__(self,name):
        self.name=name

s1=student("swasti")
print(s1.name)
del s1.name
print(s1.name)

class Account:
    def __init__(self,password,balance):
        #private use __
        self.__password=password
        
        self.balance=balance

    def reset_pass(self):
        #will work here because we are inside the class
        print(self.__password)

    def __account(self):
        print("this is a private method")


    
acc1=Account(90,1000)
print(acc1.__password) #will not work because we are outside the class
print(acc1.__account()) #will not work because we are outside the class

