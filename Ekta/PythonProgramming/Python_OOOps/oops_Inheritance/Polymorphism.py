class Father:
    def __init__(self,f_name,f_car):
        self.fathername=f_name
        self.fathercar=f_car

    def show_father_details(self):
        print("Father Name : ",self.fathername)
        print("Fathers Car : ",self.fathercar)
    
    def greetings(self):
        print("-----Hello, I am the father. You are in fathers class.-----")

class Son(Father):
    def __init__(self,s_name,f_name,f_car):
        super().__init__(f_name,f_car) #super() is used to call the constructor of the parent class and it is used to access the attributes and methods of the parent class in the child class. It is used to avoid the ambiguity in the child class when there are same attributes or methods in both parent and child class. It is also used to call the constructor of the parent class in the child class when we have defined a constructor in the child class. It is also used to call the method of the parent class in the child class when we have defined a method with same name in both parent and child class.
        self.sonname=s_name

    def show_son_name(self):
        print("Son Name : ",self.sonname)
    
    def show_family_details(self):
        print("Family Details ")
        self.show_father_details() #accessed method of parent class in child class using self keyword
        self.show_son_name() #accessed method of child class in child class using self keyword
    
    def greetings(self):
        print("-----Hello, I am the son. You are in son's class.-----")

obj=Son("Rohan","Mr. Rajesh","BMW")   #created object of the child class and passed arguments to the constructor of the child class
obj.show_family_details()
print("Using object, father details accessed ")
obj.show_father_details()
print("Using object, Child details accessed ")
obj.show_son_name()   #accessed method of child class which is calling method of parent
obj.greetings()