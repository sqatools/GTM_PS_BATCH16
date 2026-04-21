# inheritance : when one class aquire the property of another class, then it is called inheritance.

# 1. Single Inheritance :  Class A -> class B

class Father:
    def __init__(self, f_name, f_car):
        self.f_name = f_name
        self.f_car = f_car

    def show_father_details(self):
        print("Father Name :", self.f_name)
        print("Father car:", self.f_car)


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


obj = Son("Mohit", "Mr Raghav", "BMW")
obj.ShowFamilyDetails()




