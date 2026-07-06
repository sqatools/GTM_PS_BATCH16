

class Test:
    def __init__(self, name,age):
        print("constructor called")
        print("address of obj by self", id(self))
        self.name = name
        self.age = age 
        

    

t1 = Test("Ramesh", 28)
print("-----address of t1 outside of class", id(t1))
print(t1.name)
t2 = Test("manisa", 29)
print("-----address of t2 outside of class", id(t2))
print(t2.name)



def myf(a,b):
    a+b

myf(10,20)


'''class - Car
self - comnstructor parameter
car1 - obj'''

number = 100

print("number-", number)

def my_number():
    global number
    number = 200

my_number()
    
print("out func number-", number)


a=10
b=5

c=a%b

print(c)



def my_func(a,b):
    add = a+b
    print("add inside func",add)
    return add

result = my_func(10,20)
#print(add)

mult = result*2

print(mult)

