#date 30th march

def greeting(msg):
    print(msg)

msg = "hi"
greeting(msg)
greeting("good morning")

def addition(n1, n2):
    print("addition :", n1+n2)

#pass by value
addition(1,5)

addition(100,675)

#pass by refrence
x= 1009
y= 8990

addition(x, y)

#fixed output
def hello():
    print("hello world")

hello()

#function with default parameter

def multiplication(n1, n2, n3=10):
    print(f"{n1}*{n2}:", n1*n2)
    print(f"{n3}*{n2}:", n2*n3)

#n3 default

multiplication(6,5)

#n3 value changed

multiplication(6,5,9)