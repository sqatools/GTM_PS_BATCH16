# abstraction : When we show the overview information about any application and hide internal architecture and code
# design, then it is called abstraction.
# to achive abstraction in python we define the method in one class and impliment those method in chid class.

from abc import abstractmethod

class Animal:
    @abstractmethod
    def name(self):
        pass
    
    @abstractmethod
    def voice(self):
        pass

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
obj.breed()