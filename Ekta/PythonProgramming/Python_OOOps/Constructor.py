class Myclass:
    name="Suresh" #class variable 
    def __init__(self,name): #local variable we can call it directly
        print(name) 
        print(self.name) #accessing class variable

obj=Myclass("Radhika")