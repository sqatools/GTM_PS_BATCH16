from abc import abstractmethod
#abc is module which is used to create abstract class and abstract method in python. It is used to create a class which cannot be instantiated and it is also used to create a method which must be implemented in the child class. It is used to achieve abstraction in python. Abstraction is the process of hiding the implementation details and showing only the functionality to the user. It is one of the fundamental concepts of object oriented programming.
#we can directly create abstarct methods without using annotations also but it is a convention to use @abstractmethod decorator to create abstract method in python because it is more readable and it is also used to indicate that the method is an abstract method and it must be implemented in the child class.
#abc is abstract base class which is used to create abstract class in python. It is a built-in module in python and it is used to create abstract class and abstract method in python. It is used to achieve abstraction in python. Abstraction is the process of hiding the implementation details and showing only the functionality to the user. It is one of the fundamental concepts of object oriented programming.   
class Animal:
    @abstractmethod
    def name():
      pass  
    @abstractmethod
    def voice():
      pass 
    @abstractmethod
    def breed():
        pass

class lion(Animal):
    def name(self):
        print("Sheru")

    def voice(self):
        print("Roar")

    def breed(self):
        print("Panthera leo") 

obj = lion()  #created object of the child class and called the methods of the child class which are implemented from the abstract class
obj.name()
str1="Hi"
str1.lower()  #lower() is a method of string class which is used to convert the string to lowercase and it is implemented in the string class which is a built-in class in python. It is an example of abstraction because we are using the method without knowing the implementation details of the method. We are only interested in the functionality of the method which is to convert the string to lowercase. We are not interested in how the method is implemented. We are only interested in what the method does.

  