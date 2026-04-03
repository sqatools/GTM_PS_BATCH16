"""
def functionName(param):
    code

"""
# declare function/ create custom function
def Greeting(msg):
    print(msg)

Greeting("Very good Evening")
Greeting("Very good morning")


def addition(n1, n2):
    print("addition of values :", n1+n2)

# Pass by value: It means pass the values to the parameter.
addition(10, 20)
addition(100, 500)


# Pass by Reference :  It means pass by reference of third element.
x = 1000
y = 2000
addition(x, y)


# function without parameter 
def hello():
    print("Hello word")

print("_"*50)
hello()
hello()
hello()


print("_"*50)
#######################################
# function with default parameters.

def multiplication(n1, n2, n3=10):
    print(f"n1: {n1} * n2: {n2}:", n1*n2)
    print(f"n1 :{n2} * n3: {n3}:", n3*n2)

# n3 will keep default value as n3=10
multiplication(5, 6)

<<<<<<< HEAD
# update the default value of n3 from 10 to 7
multiplication(5, 6, 7)

<<<<<<< HEAD

# function with return statement
def get_square(n):
    return n**2


output = get_square(5)
print("square of 5 :", output) # square of 5 : 25


print("_"*40)
# return keyword break the function execution immdiately.
def get_sum_values(n):
    sum = 0
    for i in range(1, n+1):
        print(i)
        if i == 8:
            return sum
        sum = sum + i
        

    
sum_result = get_sum_values(10)
print("sum of values :", sum_result)


def addValues(n1, n2):
    return n1+n2

def multiplication(n1, n2):
    return n1+n2

def subtraction(n1, n2):
    return n1-n2

def division(n1, n2):
    return n1//n2

def calculator(option, num1,num2):
    if option == 1:
        r1 = addValues(num1, num2)
        print("Addition :", r1)

    elif option == 2:
        r2 = multiplication(num1, num2)
        print("multiply output :", r2)

    elif option == 3:
        r3 = subtraction(num1, num2)
        print("subtraction output :", r3)

    elif option == 4:
        r4 = division(num1, num2)
        print("Division result :", r4)

print("_"*50)
calculator(1, 30, 40)

=======
#########################################


print("Hello World")
>>>>>>> 8e9c9d4a8453716da6f1554b12f6cc4c2c36633e
=======
# return method
def add():
    return 10

add()
>>>>>>> ef572c00e68578586ad3128158aeb5530ceb3e53
