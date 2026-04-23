# . means from current location, .. means from parent location, ... means from grand parent location and so on. It is used to import modules from the same package or from the parent package. It is also used to avoid circular imports when two or more modules are importing each other. It is also used to avoid ambiguity when there are multiple modules with same name in different packages. It is also used to avoid confusion when there are multiple modules with same name in the same package. It is also used to avoid confusion when there are multiple modules with same name in the parent package. It is also used to avoid confusion when there are multiple modules with same name in the grand parent package and so on.   
from class_A import A
class B(A):
    def method_B(self):
        print("This is method B of class B")
        