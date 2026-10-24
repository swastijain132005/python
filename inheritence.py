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