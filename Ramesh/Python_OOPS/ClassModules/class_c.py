from class_B import B

class C(B):
    def method_C(self):
        print("---Welcome to calss C---")
    
obj = C()
obj.method_B()
obj.method_A()
obj.method_C()