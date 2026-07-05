class Grandfather:
    def __init__(self,gfname,gfland):
        self.gfname = gfname
        self.gfland= gfland

    def show_gf_details(self):
        print(f"name of the gf is {self.gfname} and land is {self.gfland}") 

class Father(Grandfather):
    def __init__(self,fname,fcar,gfname,gfland):
        super().__init__(gfname,gfland)
        self.fname = fname
        self.fcar = fcar

    def show_father_details(self):
        print(f"The father name is {self.fname} and the car is {self.fcar}")

class Child(Father):

    def __init__(self,son,fname,fcar,gfname,gfland):
        super().__init__(fname,fcar,gfname,gfland)
        self.son = son


    def show_son_details(self):
        print(f'the name of the son is {self.son}')

    def all_details(self):
        self.show_gf_details()
        self.show_father_details()
        self.show_son_details()    

obj = Child("Anindya","Arun","Bollero","Lolit","100cr")

obj.all_details()


