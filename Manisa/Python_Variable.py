a = 10
b = 30
# a is a variable that holds the value 10
# = is the assignment operator that assigns the value on the right to the variable on the left
# 10 is the value that is assigned to the variable a

print ("value of a is ", a)
print ("value of b is ", b)
print ("value of a is:", a, id(a))
print ("value of b is:", b, id(b))

#multiple assignment, different values to different variables at a time
x, y, z = 50, 60, 70
print ("value of x is:", x, id(x))
print ("value of y is:", y, id(y))
print ("value of z is:", z, id(z))

#assign one value to three different variable
p = q = r =100
print ("value of p is:", p)
print ("value of q is:", q)
print ("value of r is:", r)
print ("value of p, q, r, is:", p, q, r)

#rules to declare a variable
"""
1. can not contain space in a variable name
a b = 40 : invalid
a_b = 40 : correct

2. variable name can not start with a number 
1_var =50 : invalid
var1 =50 : correct

3. variable name can not contain special characters except underscore
a@b = 50 : invalid
a_b = 50 : correct

4. no specific length for variable name but it should be meaningful

5.variable name are case sensitive
var = 50 : correct
Var1 = 60 : correct

6. reserved keywords can not be used as variable name
if = 50 : invalid
if_ = 50 : correct

7. variable name should not be same as function name
print = 50 : invalid
print_ = 50 : correct

"""


#math operations with variables
num1 = 20
num2 = 10

#addition
num3 = num1 + num2
print ("addition valu:", num3)

#subtraction
print ("subtraction value:", num1-num2)

#multiplication
print ("multiplication value:", num1*num2)

#division
print ("division value:", num1/num2) #output:2.0
print ("floor division value: // value", num1//num2) #output: 2

#square and cube
print ("square value:", num1**2)
print ("cube value:", num1**3)

#compare value of variables
y1 = 50
y2 = 60
y3 = 50
print ("is y1 equal to y2?", y1 == y2) #output: False
print ("is y1 equal to y3?", y1 == y3) #output: True
print ("is y2 equal to y3?", y2 == y3) #output: False