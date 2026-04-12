#function with return statement
def get_square(n):
    return n**2

output = get_square(5)
print("square of 5 :", output)

#return keyword break the function execution immediately with returning a value
def get_sum_value(n):
    sum = 0
    for i in range(1, n+1):
        print(i)
        
        if i ==5:
            return sum
        sum =sum+i
        
sum_result = get_sum_value(10)
print("sum of values:", sum_result)

#calculator with function

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 != 0:
        return num1 // num2
    else:
        return "Error: Division by zero is not allowed."
    
def calculator(num1, num2, operation):
    if operation == "add":
        return add(num1, num2)
    elif operation == "subtract":
        return subtract(num1, num2)
    elif operation == "multiply":
        return multiply(num1, num2)
    elif operation == "divide":
        return divide(num1, num2)
    else:
        return "Error: Invalid operation."
    
calculator_result = calculator(10, 5, "divide")
print("Calculator result:", calculator_result)


#function variable
"""
global variable : variable declared outside of the function
                  we can use global variable across the function in the file
                  or outside of the file

non local variable :local variable to all inner function/inside the function
                    can not use outside of the function

local variable : declared inside the function, scope is limited to the function
                 cannot use outside of the function

"""

#global variable

var_x = 6

def function():
    #local variable
    var_y = 8
    print("global variable:", var_x)
    print("local variable:", var_y)

function()

#non local func

var_z = 10

def outer_function():
    #non local variable
    var_a =200
    print("value of a:", var_a)
    print("value of z", var_z)

    def inner_function():
        var_b = 400
        print("non local variable:", var_a)
        print("local variable:", var_b)
        print("value of z", var_z)

    inner_function()

outer_function()