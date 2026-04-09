"""
1. Number
    i) integer
    ii) float

2. Sequential
    i) string
    ii) List
    iii) Tupple

3. dict
4. set
5. boolean

"""

# 1. Integer : integer only contains

n1 = 0
n2 = 2 
n3 = 987654321
print (n1, type(n1))
print (n2, type(n2))
print (n3, type(n3))

# float : float contains decimal values

x1 = 0.0
x2 = 0.3
x3 = 45.6678889
x4 = 8765.84865
print(x1, type(x1))
print(x2, type(x2))
print(x4, type(x4))
print(x3, type(x3))


# string

s1 = "Hello"
s2 = 'Python'
s3 = """We are Learning Python"""
s4 = '''Python learning is fun'''

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))

"""

 0   1   2   3   4   5 
 P   Y   T   H   O   N
-6  -5  -4  -3  -2  -1

"""
s5 = "Python"
print(s5[2])
print(s5[-3])


# list : list can store any type of data. we can modify it
# any point of time 

l1 = [4, 5, 6]
l2 = [3, 4.5, 'Hello', [4, 5, 7], (4, 6), {'a' : 123}, {3, 5, 6}, True]

print(l1, type(l1))
print(l2, type(l2))

# list follows same positive and negative indexing as like string

print (l1[2])
print(l2[3])
print(l2[3][1])

l1.append (30)
print (l1)


# tuple : tuple datatype can store any type of data like list 
# but we can update the tuple data.

tup1 = (5, 7, 8)
tup2 = (10, 3.56, 'INDIA', (4,7), [4,7], {'a' : 567}, {5, 6, 7}, False)

print(tup1, type(tup1))
print(tup2, type(tup2))

# tuple follows same positive and negative indexing as like string and list


## Dictionary : 
# Dict store values in key values {key : value}
# dict only contains immutable data as key, int float, string, tupple, boolean.
# dict contain any type of data as value 
# dict contain only unique keys


dict1 = {'a': 123, 'b' : 456, 'c' : 789}
print(dict1, type(dict1))
print(dict1['b'])


dict2 = {
    23 : 5.6,
    4.5 : "Hello",
    "python" : [6, 7, 8],
    (5, 7, 8) : {'P' : 789, 'Q' : 45, 'R' : 123},
    True : (4, 5, 67),
    23 : 500
}

print(dict2)

# Set data : it only contains values, duplicate data is not allowed 
# Store value in random order 
# mutable datatypes are not allowed list , dict, set

set1 = {5, 7, 8, 7, 3.5, 'Hello', (5, 6, 7), True}
print(set1, type(set1))

## Boolean = boolean store value as True or false

b1 = True
b2 = False

print (b1 == b2)

a1 = 30
a2 = 40

print (a1 == a2)


## type data conversion

str1 = "Hello"
l1 = list(str1)

print(l1)


str2 = "6789"
num = int(str2)
print(num, type(num))

## Integer to string 

num1 = 6787769
s1 = str(num1)
print(s1, type(s1), s1[-1])