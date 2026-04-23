from class_B import B
class C(B):

    def method_C(self):
        print("This is method C of class C")

object_c=C()  #created object of class C
object_c.method_A()  #accessed method of class A using object of class C
object_c.method_B()  #accessed method of class B using object of class C
object_c.method_C()  #accessed method of class C using object of class C