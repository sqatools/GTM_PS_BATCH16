# when on person perform multiple task, then it is called polymorphism.
# 1. method overrding ->  when parent and child class have method with same, and child class method will override parent
#                         class method.


# 2. Method overloading: one class have 2 method with same name and different parameter, then it is called method 
#                   overloading.
#                   -> method overloading is not supported in Python.
#                   -> Python only consider the latest defined method.

class Father:
    def __init__(self, f_name, f_car):
        self.f_name = f_name
        self.f_car = f_car

    def show_father_details(self):
        print("Father Name :", self.f_name)
        print("Father car:", self.f_car)

    def greeting(self):
        print("--- Welcome to Father class ----")

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
        print("--- Welcome to Son class ----")


    def addition(n1, n2):
        print("addition of 2 number :", n1+n2)


    def addition(m1, m2, m3):
        print("Addition of 3 numbers :", m1+m2+m3)


obj = Son("Mohit", "Mr Raghav", "BMW")
obj.ShowFamilyDetails()
obj.greeting()
obj.addition(10, 20)




