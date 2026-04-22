#class name 
class Car:
    CompanyName="TATA"
    #Constructor 
    def __init__(self,car_name,car_price,car_model):
        print("Constructor called automatically")
        self.CarName=car_name #public variable which can be accessed outside the class and inside the class
        self._CarPrice=car_price #protected variable which can be accessed inside the class and outside the class but it is not recommended to access protected variable outside the class because it is a convention to use protected variable inside the class only and it
        self.__CarModel=car_model #private variable which can be accessed inside the class only and it is not recommended to access private variable outside the class because it is a convention to use private variable inside the class only and it is also used to hide the data from the user and it is also used to achieve encapsulation in python.
    #instance method
    def ShowCarName(self):
        print("Car name is ",self.CarName)
    #instance method
    def _ShowCarPrice(self):
        print("Car price is ",self._CarPrice)  
    #instance method
    def __ShowCarModel(self):
        print("Car model is ",self.__CarModel)  
    #Accessed methods inside method 
    def ShowCarDetails(self):
        print("Car name is ",self.ShowCarName())
        print("Car price is ",self.ShowCarPrice())  
        print("Car model is ",self.ShowCarModel())

    

obj=Car("BMW",1000000,"X5")   #created object of the class and passed arguments to the constructor
obj.ShowCarName()
obj._ShowCarPrice()  #accessed protected method outside the class but it is not recommended to access protected method outside the class because it is a convention to use protected method inside the class only
obj._Car__ShowCarModel()  #accessed private method outside the class but it is not recommended to access private method outside the class because it is a convention to use private method inside the class only and it is also used to hide the data from the user and it is also used to achieve encapsulation in python. It will give an error because private method cannot be accessed outside the class.
print("Accessed private variable outside the class using class name---> ",obj._Car__CarModel) #accessed private variable outside the class using name mangling but it is not recommended to access private variable outside the class because it is a convention to use private variable inside the class only and it is also used to hide the data from the user and it is also used to achieve encapsulation in python. It will give an error because private variable cannot be accessed outside the class.