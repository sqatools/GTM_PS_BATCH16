i,j=15,25 #global variable
class Myclass():
    a,b=100,200 #class variables or static variables or class attributes. These variables are shared among all the instances of the class. They are defined inside the class but outside any method. They are accessed using self keyword.
    def add(self):
        c=self.a+self.b
        print("Addition of a and b is ",c)
    def multiply(self):
        c=self.a*self.b
        print("Multiplication of a and b is ",c)
    def add1(self,x,y):
        c=x+y
        print("Addition of x and y is ",c)
        print("Addition of i and j is",i+j)
        

obj1=Myclass()   #created object of the class
obj1.add()   #accessed add method using object of the class
obj1.multiply()   #accessed multiply method using object of the class
obj1.add1(500,500)   #accessed add1 method using object of the class