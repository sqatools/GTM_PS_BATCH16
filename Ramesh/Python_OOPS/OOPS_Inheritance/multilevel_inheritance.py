# inheritance : when one class aquire the property class, then it is called inheritance.

#1. Multilevel Inheritance : Class A -> Class B -> Class C

class GrandFather:
    def __init__(self, gf_name, gf_property):
        self.gf_name = gf_name
        self.gf_property = gf_property

    def show_GrandFather_Details(self):
        print("Grand Father Name :", self.gf_name)
        print("Grand Father Property:", self.gf_property)


class Father(GrandFather):
    def __init__(self, f_name, f_car, gf_name, gf_property):
        super().__init__(gf_name, gf_property)
        self.f_name = f_name
        self.f_car = f_car


    def show_father_details(self):
        print("Father Name :", self.f_name)
        print("Father Car :", self.f_car)


class Son(Father):
    def __init__(self, son_name, f_name, f_car, gf_name, gf_property):

        # initialize the parent class constructor into child class
        super().__init__(f_name, f_car, gf_name, gf_property)
        self.son_name = son_name

    def show_son_name(self):
        print("Son Name :", self.son_name)

    def ShowFamilyDetails(self):
        self.show_GrandFather_Details()
        self.show_father_details()
        self.show_son_name()


obj = Son("Mohit", "Mr Raghavir", "BMW", "Dayaram", "100 Acr Land")
obj.ShowFamilyDetails()