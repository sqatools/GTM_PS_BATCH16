class Father:
    def __init__(self,fname,fcar):
        self.fname = fname
        self.fcar=  fcar

    def show_father_details(self):
        print(f'the name of the father is {self.fname} and the car is {self.fcar}')


class Mother:
    def __init__(self,mname):
        self.mname = mname

    def show_mother_details(self):
        print(f'the name of the mothet is {self.mname}')


class Child(Father,Mother):
    def __init__(self,son,fname,fcar,mname):
        super().__init__(fname,fcar)
        self.son = son
        self.mname = mname

    def show_son_details(self):
        print(f'the son name is {self.son}')    

    def all_details(self):
        self.show_father_details()
        self.show_mother_details()
        self.show_son_details()

obj = Child('Anindya',"Arun","Bolleto","Uma")

obj.all_details()




