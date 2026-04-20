"""
Class: class is blue print of an object where it contains method/attribute/variables.
Object: object is an entity that access all properties defined in the class.
Constuctor: Constructor that initialize, memory for the object is being created.
        ->  There is default constructor being called, whenever we create object of the class.
        ->  If we provide parameter to constructor, then it is called parametrize construtor.
method : when define any function inside the class then become method.


"""
# class
class Animal:
    # class variable
    Zooname = "Jungle"

    # constructor
    def __init__(self, animal_name, animal_age):
        print("-----Welcome to Animal Class Constructor-----")

        self.Name=animal_name
        self.Age=animal_age 

    # instance method
    def animal_details(self):
        print("Animal name:",self.Name)
        print("Animal Age:",self.Age)

object=Animal("Tiger",20)
object.animal_details()
print("Class Variable ",object.Zooname)

    
  






