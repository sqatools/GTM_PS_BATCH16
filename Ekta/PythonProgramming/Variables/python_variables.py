a=10
b=50
c=10


print("Value of a is:", a)
print("Value of b is:", b)

print("***** Checking memory address of two variables with same value: *****")
print("Memory address of a:", id(a))
print("Memory address of c:", id(c))
print("Memmory address of b:",id(b))

 ### Assign different values to different variables at sinle declaration ###
x,y,z=100,200,300
print("Value of x,y,z --->  ", x, y, z)
 
 #Assign same value to different variables #

p=q=r=500
print("Value of p,q,r --->", p,q,r)

# Math Operation on numebrs #
number1=425
number2=200
print("Addition of number1 and number2 is :", number1+number2)
print("Subtraction of two numbers ", number1-number2)
print("Multiplication of two numbers ", number1*number2)
print("Division of two numbers with / ", number1/number2)
print("Division of two numebrs with // ", number1//number2)
print("Square of number1 is ", number1**2)
print("Cube of number1 is ", number1**3)

x=100
y=222
z=100
print("Compare x and y ", x==y)
print("Compare y and z", y==z)
print("Compare x and z", x==z)

