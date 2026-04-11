def greeting(msg):
    print(msg)  

greeting("Good Morning")
greeting("Good Evening")        


def addition(n1, n2):
    print("Addition of values:", n1+n2)

addition(10, 20)
addition(100, 200)  

# Pass by Reference :  It means pass by reference of third element.
x = 1000
y = 2000
addition(x, y)


# function without parameter 
def hello():
    print("Hello word")     

print("_"*50)
hello()


print("_"*50)
#######################################
# function with default parameters.

def multiplication(n1, n2, n3=10):
    print(f"n1: {n1} * n2: {n2}:", n1*n2)
    print(f"n1 :{n2} * n3: {n3}:", n3*n2)

# n3 will keep default value as n3=10
multiplication(5, 6)

# update the default value of n3 from 10 to 7
multiplication(5, 6, 7)





def call(p1, p2):
    print ("addition:",p1 + p2)

call(12, 50)


