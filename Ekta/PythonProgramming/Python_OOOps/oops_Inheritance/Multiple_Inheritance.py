class Father:
    def __init__(self,f_name,f_car):
        self.fathername=f_name
        self.fathercar=f_car

    def show_father_details(self):
        print("Father Name : ",self.fathername)
        print("Fathers Car : ",self.fathercar)

class Mother:
    def __init__(self,m_name):
        self.mothername=m_name
        

    def show_mother_details(self):
        print("Mother Name : ",self.mothername)
      

class Son(Father,Mother):
    def __init__(self,s_name,f_name,f_car,m_name):
        super().__init__(f_name,f_car) #super() is used to call the constructor of the parent class and it is used to access the attributes and methods of the parent class in the child class. It is used to avoid the ambiguity in the child class when there are same attributes or methods in both parent and child class. It is also used to call the constructor of the parent class in the child class when we have defined a constructor in the child class. It is also used to call the method of the parent class in the child class when we have defined a method with same name in both parent and child class.
        #Mother.__init__(self,m_name) #accessed constructor of second parent class in child
        self.sonname=s_name
        self.mothername=m_name

    def show_son_name(self):
        print("Son Name : ",self.sonname)
    
    def show_family_details(self):
        print("Family Details ")
        self.show_father_details() #accessed method of parent class in child class using self keyword
        self.show_son_name()
        self.show_mother_details() #accessed method of child class in child class using self keyword

obj=Son("Rohan","Mr. Rajesh","BMW","Mrs Priya")   #created object of the child class and passed arguments to the constructor of the child class
obj.show_family_details()
print("Using object, father details accessed ")
obj.show_father_details()
print("Using object, son details accessed ")
obj.show_son_name()   
print("Using object, mother details accessed ")
obj.show_mother_details()  #accessed method of child class which is calling method of parent