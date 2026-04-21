class Myclass:
#self is keyword which says myfunction is part of Myclass. It is used to access the attributes and methods of the class in python. It binds the attributes with the given arguments. It is the first parameter of any function in the class.  
    def myfunction(self):
        print("This is my function")
#here we passed parameter name as argument and we can access it using self keyword. It is used to initialize the attributes of the class. It is called when an object of the class is created. It is a special method in python. It is also known as constructor in python. It is used to initialize the attributes of the class. It is called when an object of the class is created. It is a special method in python. It is also known as constructor in python.
    def display(self,name):
        print("Hello",name)
#access methods by creating object of the class. We can create multiple objects of the class and access the methods using those objects. We can also pass different arguments to the methods using different objects. It is used to create multiple instances of the class and access the methods using those instances. It is also known as object in python.
obj=Myclass()   #created object of the class
obj.myfunction()   #accessed method using object of the class        
obj.display("Ekta")  #accessed display method using object of the class    