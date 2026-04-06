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

# function with return statement 
def get_square(n):
    return(n**2)

output = get_square(5)
print(output)


# return keyword break the function execution immidiately.

def get_sum_value(n):
    sum = 0
    for i in range(1, 10):
        print(i)
        if i == 4:
            return sum
        sum += i

sum_result = get_sum_value(10)
print(sum_result)

print("_"*50)

def addValues(n1, n2):
    return n1+n2
def mulitiplication(n1,n2):
    return n1 * n2
def subtraction(n1, n2):
    return n1 - n2
def division(n1, n2):
    return n1 // n2

def calculator(option, num1, num2):
    if option == 1:
        r1 = addValues(num1, num2)
        print(r1)
    elif option == 2:
        r2 = multiplication(num1, num2)
        print(r2)
    elif option == 3:
        r3 = subtraction(num1, num2)
        print(r3)
    elif option == 4:
        r4 = division(num1, num2)
        print(r4)


print("_"*40)
calculator(1, 30, 40)

