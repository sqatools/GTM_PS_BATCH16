# when one person perform multiple task, than it is called pollymorphism.
# 1. method overriding -> when parent and child clas have method with same, and child class method will override parent


# 2. Method : one class have 2 method with the same name and different 

class Father:
    def __init__(self, f_name, f_car):
        self.f_name = f_name
        self.f_car = f_car


    def show_father_details(self):
        print("Father Name :", self.f_name)
        print("Father Car :", self.f_car)

    
    def greeting(self):
        print("---Welcome to Father class---")


class Son(Father):
    def __init__(self, son_name, f_name, f_car):

        # initialize the parent class constructor into child class
        super().__init__(f_name, f_car)
        self.son_name = son_name

    def show_son_name(self):
        print("Son Name :", self.son_name)

    def ShowFamilyDetails(self):
        self.show_father_details()
        self.show_son_name()

    def greeting(self):
        print("---Welcome to Son class---")


obj = Son("Mohit", "Mr Raghavir", "BMW")
obj.ShowFamilyDetails()
obj.greeting()