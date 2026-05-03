## function is a block of code that we write and we can use it repeatedly in our program. It helps us to avoid code duplication and makes our code more organized and easier to read.
## def function_name(parameters):
##     # function body

# defining a function
def greet(name):
    print(f"Hello, {name}!")

# calling the function
greet("Alice")
greet("Bob")

## function with multiple parameters

def add(a, b):
    print("adding two numbers", a+b)
 
add(5, 3)  ## pass by Value

## Pass by reference
x = 2314
y=86

add(x,y)  ## pass by reference

## fucntion without parameters
def say_hello():
    print("Hello, World!")

say_hello()

say_hello()
say_hello()

print("*"*50)

## function with default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  ## will use default value "Guest"
greet("Alice")  ## will use the provided value "Alice"

def multiplication( n1, n2, n3= 10):
    print(f"n1: {n1}, n2: {n2}, n3: {n3}")

multiplication(5, 3)  ## will use default value for n3
multiplication(5, 3, 2)  ## will use provided value for n3


## function with return statement
def square(num):
    return num**2
result = square(4)
print("Square of number is:", result)


### return keyword break the function execution immeditely and return the value to the caller. It can be used to return any type of value, including numbers, strings, lists, or even other functions. If no return statement is provided, the function will return None by default.    

print("*"*50)
def sum_of_numbers(n):
    sum= 0
    for i in range(1, n+1):
        sum += i
        if i == 5:
            return sum  ## will return the sum when i is 5 and break the function execution immediately      
print(sum_of_numbers(10))  ## will return 15, which is the sum of numbers from 1 to 5


