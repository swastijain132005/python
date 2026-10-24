class car :
    @staticmethod
    def drive():
        print("driving")

class toyotacar(car):
    def __init__(self,model):
        self.model=model

    def hello(self):
        print("hello",self.model)

t1=toyotacar("camry")
t1.drive()

class bike:
    def __init__(self,brand):
        self.brand=brand

class vehicle(bike, car):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model

class student:
    def __init__(self,phy,cnem,math):
        self.phy=phy
        self.cnem=cnem
        self.math=math

    @property
    def percentage(self):
            return str((self.phy + self.cnem + self.math) / 3)+"%"

st1=student(90,80,70)
print(st1.percentage)
st1.phy=95
print(st1.percentage)#if we change the value of phy then percentage will also change because we are using property decorator

class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def showDetails(self):
        print("Role:",self.role)
        print("Department:",self.dept)
        print("Salary:",self.salary)

class Enginner(Employee):
    def __init__(self,role,dept,salary,project):
        super().__init__(role,dept,salary)
        self.project=project
    def showDetails(self):
        super().showDetails()
        print("Project:",self.project)


class Enginner2(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Enginner","IT",100000)


e1=Enginner("Engineer","IT",100000,"Project1")
e1.showDetails()
e2=Enginner2("Raj",25)
e2.showDetails()