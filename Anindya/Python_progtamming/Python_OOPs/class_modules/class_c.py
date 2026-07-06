from class_b import B

class C(B):
    def class_c(self):
        print("This is class C")


obj = C()

obj.class_a()
obj.class_b()
obj.class_c()

