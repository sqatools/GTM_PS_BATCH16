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
