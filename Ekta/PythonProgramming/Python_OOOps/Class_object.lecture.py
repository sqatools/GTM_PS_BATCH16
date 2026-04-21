#class name 
class Car:
    CompanyName="TATA"
    #Constructor 
    def __init__(self,car_name,car_price,car_model):
        print("Constructor called automatically")
        self.CarName=car_name
        self.CarPrice=car_price
        self.CarModel=car_model
    #instance method
    def ShowCarName(self):
        print("Car name is ",self.CarName)
    #instance method
    def ShowCarPrice(self):
        print("Car price is ",self.CarPrice)  
    #instance method
    def ShowCarModel(self):
        print("Car model is ",self.CarModel)  
    #Accessed methods inside method 
    def ShowCarDetails(self):
        print("Car name is ",self.ShowCarName())
        print("Car price is ",self.ShowCarPrice())  
        print("Car model is ",self.ShowCarModel())

    @classmethod
    def showCompanyName(cls):
        print("Company Name ",cls.CompanyName)

    @staticmethod
    def get_factorial(num):
        fact=1
        for i in range(num,0,-1):
            fact=fact*i
        
        return fact
    

obj=Car("BMW",1000000,"X5")   #created object of the class and passed arguments to the constructor
obj.ShowCarName()   
obj.ShowCarPrice()
obj.ShowCarModel()
Car.showCompanyName() #Access classmethod with class name
print("Factorial of number is--> ",Car.get_factorial(4)) # Access static method with class name
    