# Class : Like a blueprint of an object which defines the properties and behaviors of the object.
# Object : An instance of a class which has its own state and behavior.
# OOPs : Object Oriented Programming System is a programming paradigm which is based on the concept of objects and classes.
# Inheritance : It is a mechanism in which a new class is derived from an existing class. 
# Polymorphism : It is the ability of an object to take many forms. 
# It allows us to use a single interface to represent different types of objects.
# Encapsulation : It is the mechanism of hiding the internal details of an object 
# only exposing the necessary information to the outside world.
# Abstraction : It is the process of hiding the implementation details and showing only the functionality to the user.

# Example of a class and object in Python:

class dog:

    species = "Canis familiaris"  # class variable which is shared by all instances of the class

    def __init__(self, name, age):   # constructor method which is called when an object is created
        self.name = name
        self.age = age

    def bark(self):   # method which defines the behavior of the object
        return f"{self.species} says Woof!"
    
# Creating an object of the class dog
my_dog = dog("Buddy", 3)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
print(my_dog.bark())  # Output: Canis lupus familiaris says Woof!

result = my_dog.bark()
