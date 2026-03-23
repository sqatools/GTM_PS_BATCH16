a = 10
b = 30

if a == b :
    print("Both numbers are equal")
else:
    print("Both number are not equal")

"""
numTrue = input("Enter your value :")
if int(num)%2 == 0:
    print("This is even number")
else:
    print("This is odd number")
"""
"""
# In and condition both the condition should be True
cond1 and cond2
True and False :  False
False and True :  False
False and False :  False
True and True : 

# in or logic any one condition can be true
cond1 or cond2
True or False :  True
False or True :  True
False or False :  False
True or True : True

> : greater than
<:  less than
>= : greater equal
<= : less than equal
== : equal opertor
!= : not equal operator
in : in operator
not in : not in opereator
"""
print("#"*50)
x = 30
y = 50
z = 60

if x > y and x > z:
    print("X has greater value")
else:
    print("X doesn't have greater value")


#####################################
print("#"*50)
# if - elif - else

a = 100
b = 100
c = 80

if a > b and a > c:
    print("A has greater value:", a)
elif b > a and b > c:
    print("B has greater value :", b)
elif c > a and c > b:
    print("C has greater value :", c)
else:
    print("No one have greater value")


##############################
# Nested If condition
"""
if cond1:
    code
    if cond2:
        code
    else:
        code
else:
    code
"""
print("#"*40)
round1 = "fail"
round2 = "fail"
intern = "fail"

if round1 == "pass":
    print("congrats 1st round is cleared")
    if round2 == "pass":
        print("congrats 2nd round is cleared")
    else:
        print("sorry failed in 2nd round.")
else:
    print("sorry failed in 1st round.")
    if intern == "pass":
        print("congrats you passed trainee round")
    else:
        print("sorry failed in trainee round.")


############################
print("#"*40)
list1 = [50, 60, 70, 80]
val = 50
if val in list1:
    print("Val is available:", val)
else:
    print("value is not available", val)


############################
print("#"*40)

str1 = "Hello we are Java Learning Python"
if "Java" not in str1:
    print("Java is not there")
else:
    print("Java is avaiable")


############################
print("#"*40)
# one line if condition
num = 11
result = "even" if num%2 ==0 else "odd"
print("result :", result)

print("even" if num%2 ==0 else "odd")