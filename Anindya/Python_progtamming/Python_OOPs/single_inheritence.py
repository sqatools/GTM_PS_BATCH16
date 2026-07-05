class Father:
    def __init__(self,fname, fcar):
        self.fname = fname
        self.fcar = fcar

    def show_father_details(self):
        print(f'the father name is {self.fname} and the car is {self.fcar}')


class Child(Father):
    def __init__(self,son,fname,fcar):
        super().__init__(fname,fcar)
        self.son = son


    def show_son_details(self) :
        print(f'the son name is {self.son}')

    def all_details(self):
        self.show_father_details()
        self.show_son_details()

obj = Child("Anindya","Arun","Scoppio")

obj.all_details()
