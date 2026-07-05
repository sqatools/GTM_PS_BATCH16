class Father:
    def func(self):
        pass
    def abc(self):
        pass
    def bcd(self):
        pass

class Child(Father):
    def func(self):
        print("This is from child class func")

    def abc(self):
        print("This is from child class abc")    

    def bcd(self):
        print("This is from child class bcd")

obj = Child()

obj.func()
obj.abc()
obj.bcd()

