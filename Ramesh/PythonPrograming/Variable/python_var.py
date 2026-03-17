a = 10

b = 20
c = 10

print("value of a is ", a, id(a))
print("value of b is ", b, id(b))
print("value of c is ", c, id(c))

###### different value to different variable at a time ######

x, y, z = 50, 60, 70

print("value of x is ", x)
print("value of y is ", y)
print("value of z is ", z)

########## same value to different variable at a time ######

a = b = c = 100

print("value of a is ", a)
print("value of b is ", b)
print("value of c is ", c)

## rules to declare variable in python
"""
1. can not contain space in variable name.
a_b = 10 : invalid
a_b = 53

2. can not start variable name with number..
1_var_a = 40 : invalid
var_123_a = 50 : valid

3. can not contain  special character in variable name except _underscore

abc_$_p = 599 : invalid
_pqr_hello = "python programming"

4. there is no specific length for variable name 

k = 600
we_are_learning_python_programing = 8876987


"""
#5. variable name are case sensitive
name = "Ramesh"
Name = "Ramesh Kumar"
NAME = "Ramesh k"
namE = "Rames"
NamE = "Ram"

print(name, Name, NAME, namE, NamE)

var1 = 10
var2 = 20
var3 = "hello"
var4 = "python programming"
var5 = "we are learning python programming"


############# math operation of numbers #########

num1 = 20
num2 = 5

num3 = num1 + num2
print("addition value :", num3)
print("multiplication value :", num1 * num2)
print("division with :", num1 / num2)
print(" division with :", num1 // num2)
print("subtraction with :", num1 - num2)

#square  and cube of value
print("square on num1 :", num1 ** 2)
print("cube on num2 :", num2 ** 3)


y1 = 50
y2 = 60 
y3 = 50

#compare value of variable
print(y1 == y2)
print(y2 == y3)
print(y1 == y3)