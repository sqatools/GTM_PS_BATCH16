a = 10
# a : variable
# = : assignment
# 10 : value to assign 
b = 30
c = 10

print("value of a :", a, id(a))
# value of a : 10 140705768174792
print("value of b :", b, id(b))
# value of b : 30 140705768175432
print("value of c :", c, id(c))
# value of c : 10 140705768174792


########## different value to diff variables at a time ################
x, y, z = 50, 60, 70
print("value of x :", x) # 50
print("value of y :", y) # 60
print("value of z :", z) # 70


################# assign one value to three different variables ###########

p = q = r = 100
print("value of P:", p) # 100
print("value of q:", q) # 100
print("value of r:", r) # 100
print("value of p, q, r :", p, q, r)
# value of p, q, r : 100 100 100

## Rule to declare variable ####
"""
1. Can not contain space in variable name.
a b = 40 : invalid
a_b = 50

2. Can not start variable name with number

1_var_a = 40 : invalid
var_123_a = 50 : valid


3. Can not contain special character in variable name except _ underscore

abc_$_p = 500 : invalid
_pqr_hello = "Python Programming"


4. There is no specific length for variable name.
k = 600
we_Are_learning_Python_Programming = 87987987
"""

#5. Variable name are case sensitive.
name = "Rahul"
Name = "Mohit"
NAME  = "Raghav"
namE = "Ravi"
NamE = "Rohan"
print(name, Name, NAME, namE, NamE)
# Rahul MOhit Raghav Ravi Rohan

var1 = 40.45
var2 = 5990
var3 = 'Hello'
var4 = "Hello Python"
var5 = """We are Learnign Python"""


############# Math Operation of numbers ##############
num1 = 20
num2 = 5

# Addition 
num3 = num1 + num2
print("Addition value :", num3) # Addition value : 25

# multiplication
print("multiplication :", num1*num2) # multiplication : 100

# division

print("division with / :", num1/num2) # division with / : 4.0
print("division with //:", num1//num2) # division with //: 4

output1 = 5/2  # it will consider complete output with pointer
print("output1 :", output1) # output1 : 2.5
output2 = 5//2 # it will only consider whole number, decimal value
# will ignored.
print("output2 :", output2) # output2 : 2

# subtraction
print("Subtraction :", num1 - num2) # Subtraction : 15

# square and cube of value
print("square of num1 :", num1**2) # square of num1 : 400
print("cube of num2 :", num2**3) # cube of num2 : 125


y1 = 50
y2 = 60
y3 = 50
# compare value of variable
print(y1 == y2) # False
print(y2 == y3) # False
print(y1 == y3) # True





