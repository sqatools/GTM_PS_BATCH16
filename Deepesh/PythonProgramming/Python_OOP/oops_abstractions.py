# abstraction :  when we show the overview information about any application and hide internal architecture and code 
# design, then it is called abstraction.
# To achive abstraction in Python we defined the method in one class and impliment those method in child class.

from abc import abstractmethod

class Animal:
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def voice(self):
        pass

    @abstractmethod
    def breed(self):
        pass


class Lion(Animal):
    def name(self):
        print("Shera")

    def voice(self):
        print("Roar")

    def breed(self):
        print("African Lion")


obj = Lion()
obj.name()
# str1 = "Hello"
# str1.lower()