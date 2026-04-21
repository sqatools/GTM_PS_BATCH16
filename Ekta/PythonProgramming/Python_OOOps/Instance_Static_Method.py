class Myclass:
    def instance_method(self): #instance method is a method which is defined inside the class and it is called by creating an object of the class.       
        print("This is instance method which is called by creating an object of the class")

    @staticmethod
    def static_method():
        print("This is static method which is called without creating an object of the class")
obj=Myclass()   #created object of the class
obj.instance_method()   #accessed instance method using object of the class        
Myclass.static_method()  #accessed static method without creating an object of the class