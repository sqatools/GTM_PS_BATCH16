"""
def functionName(param):
    code

"""


def Greeting(msg):
    print(msg)

Greeting("Very Good Morning")
Greeting("Very Good Evening")

def addition(n1, n2):
    print("addition: ", n1 + n2)

addition(10, 20)
addition(100, 500)


# pass bt refference 
x = 1000
y = 2000

addition(x, y)


def hello():
    print("Hello world")

hello()
hello()
hello()


#############################################################################

# function with default parameters.

def multiplication(n1, n2, n3=10):
    print(n1 * n2)
    print(n2 * n3)

multiplication(1, 2, 5)
multiplication(4, 6)