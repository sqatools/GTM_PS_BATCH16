from math import floor


print("Hello World")
a = 10
# a : variable
# = : assignment
# 10 : value to assign 
b = 30
c = 10

print("value of a :", a, id(a))
# value of a : 10 140704539899080
print("value of b :", b, id(b))
# value of b : 30 140705768175432
print("value of c :", c, id(c))
# value of c : 10 140704539899080


x , y , z = 50, 60, 70
print("value of x :", x) # 50   
print("value of y :", y)# 60
print("value of z :", z)# 70

p = q = r = 500
print("value of P:", p) # 500    
print("value of q:", q) # 500
print("value of r:", r) # 500
print("value of p, q, r :", p, q, r)


name = "Rahul"
Name = "Mohit"
NAME = "Raghav"
namE = "Ravi"
NamE = "Rohan"
print(name, Name, NAME, namE, NamE)


var1 = 40
var_123_a = 50
_pqr_hello = "Python Programming"
print("value of var1:", var1)
print("value of var_123_a:", var_123_a)
print("value of _pqr_hello:", _pqr_hello)


num1 = 10
num2 = 20   

addition = num1 + num2
print("Addition of num1 and num2:", addition)   

subtraction = num1 - num2
print("Subtraction of num1 and num2:", subtraction)

multiplication = num1 * num2
print("Multiplication of num1 and num2:", multiplication)

division = num1 / num2
print("Division of num1 and num2:", division)   

modulus = num1 % num2
print("Modulus of num1 and num2:", modulus)

square_num1 = num1 ** 2
print("Square of num1:", square_num1)

square_num2 = num2 ** 2
print("Square of num2:", square_num2)   

cube_num1 = num1 ** 3
print("Cube of num1:", cube_num1)

cube_num2 = num2 ** 3
print("Cube of num2:", cube_num2)   

floor_division = num1 // num2
print("Floor division of num1 and num2:", floor_division)   


R1 = 5
R2 = 10     
R3 = 5
# compare values of variables
print(R1 == R2)
print(R1 == R3)
print(R2 == R3)

#---------------------------------------------------------------------------------------------

#Integer

n1 = 0
n2 = 100
n3 = 18186565163
print(n1, type(n1)) 
print(n2, type(n2)) 
print(n3, type(n3))

#----------------------------------------------------------
# Float

x1 = 0.0
x2 = 0.3    
x3 = 45.6678889
x4 = 8990809.54545

print(x1, type(x1))
print(x2, type(x2))
print(x3, type(x3))
print(x4, type(x4))

#----------------------------------------------------------
# String    

s1 = "Hello"
s2 = 'Python'
s3 = """Hello, 'Python' is a great language!"""
s4 = '''Hello, "Python" is a great language!'''

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))

"""
0  1 2 3 4 6
P  y   t   h   o   n
-6 -5  -4  -3  -2  -1 

"""

s5 = "Python"
print(s5[2])
print(s5[-3])

#----------------------------------------------------------
# List

list1 = [20, 10 ,50 ,79,90,10,40]
print(list1, type(list1))

list2 = ["Python", "Programming", "is", "fun",10, 20.5, (1, 2, 3), [4, 5, 7], (4, 6), {'a': 123}, {3, 5, 6}, True]
print(list2[6][2])
print(list2[7][1])

#----------------------------------------------------------
# Tuple 
tuple1 = (20, 10 ,50 ,79,90,10,40)
print(tuple1, type(tuple1))

tuple2 = ("Python", "Programming", "is", "fun",10, 20.5, (1, 2, 3), [4, 5, 7], (4, 6), {'a': 123}, {3, 5, 6}, True)
print(tuple2[6][2]) 
print(tuple2[7][1])

#----------------------------------------------------------
# Dictionary    
dict1 = {"name": "Rahul", "age": 25, "city": "Mumbai"}
print(dict1, type(dict1))
print(dict1["name"])
print(dict1["age"])     
print(dict1["city"])

dict2 = {"name": "Rahul", "age": 25, "city": "Mumbai", "hobbies": ["Reading", "Traveling", "Cooking"], "education": {"degree": "Bachelor's", "major": "Computer Science"}}
print(dict2["hobbies"][1])
print(dict2["education"]["major"])

