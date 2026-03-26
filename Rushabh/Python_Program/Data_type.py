
"""
1. Number 
   i). integer
   ii). float

2. Sequential
   i) string
   ii) list
   iii) Tuple
   
3. dict
4. set
5. boolean
"""

# 1. Ingeter : integer only contains whole number.

n1 = 0
n2 = 2
n3 = 78979879878798798798798
print(n1, type(n1)) # 0 <class 'int'>
print(n2, type(n2)) # 2 <class 'int'>
print(n3, type(n3)) # 78979879878798798798798 <class 'int'>

# 2. float : float contains decimal values
x1 = 0.0
x2 = 0.3
x3 = 45.6678889
x4 = 8990809.54545
print(x1, type(x1)) # <class 'float'>
print(x2, type(x2)) #<class 'float'>
print(x4, type(x4)) # <class 'float'>
print(x3, type(x3)) # <class 'float'>


print("#"*50)
# Sequential data type
# String

s1 = "Hello"
s2 = 'Python'
s3 = """We are Learning Python
its keywrods very easy to remember
"""
s4 = '''Python learning is fun'''
print(s1, type(s1)) # <class 'str'>
print(s2, type(s2)) # <class 'str'>
print(s3, type(s3)) # <class 'str'>
print(s4, type(s4)) # <class 'str'>

"""
 0  1  2  3  4  5
 P  y  t  h  o  n
-6 -5 -4 -3 -2 -1 

"""

s5 = "Python"
print(s5[2]) # t
print(s5[-3]) # h


print("#"*50)
####################
# list :  list can store any type of data. we can modify it 
# any point of time.

l1 = [4, 5, 6]
l2 = [3, 4.5, 'Hello', [4, 5, 7], (4, 6), {'a': 123}, {3, 5, 6}, True]

print(l1, type(l1)) # <class 'list'>
print(l2, type(l2)) # <class 'list'>

# list follows same +ve and -ve indexing as like string.

print(l2[2]) # Hello
print(l2[3]) # [4, 5, 7]
print(l2[3][1]) # 5

l1.append(30)
print(l1) # [4, 5, 6, 30]

print("#"*50)
####################
# tuple : tuple data type can store any types of data like list
# but we can not update the tuple data.

tup1 = (5, 7, 8)
tup2 = (10, 3.56, 'India', (4, 7), [4, 7], {'a': 567}, {5, 6, 7}, False)

print(tup1, type(tup1))
print(tup2, type(tup2))


# tuple follows same +ve and -ve indexing as like string and list
print(tup2[5]) # {'a': 567}
print(tup2[5]['a']) # 567


print("#"*50)
####################
# dictionary :
# Dict store values in keys values {key: value}
# dict only contains immutable data as key , int, float, string, tuple, boolean
# dict contains any type of data as value
# dict contains only unique keys.

dict1 = {'a': 123, 'b': 456, 'c': 789}
print(dict1, type(dict1)) # {'a': 123, 'b': 456, 'c': 789} <class 'dict'>
print(dict1['b']) # 456

dict2 = {
    23 : 5.6,
    4.5 : "Hello",
    "Python" : [6, 7, 8],
    (5, 7, 8) : {'P': 789, 'Q': 45, 'R': 123},
    True : (4, 5, 67),
    23 : 500
}

print(dict2)
print(dict2["Python"]) # [6, 7, 8]
print(dict2[(5, 7, 8)]) # {'P': 789, 'Q': 45, 'R': 123}
print(dict2.keys()) # dict_keys([23, 4.5, 'Python', (5, 7, 8), True])
print(list(dict2.keys())[3][1]) # 7

print("#"*50)
####################
# set data :  it only contains unique values, duplicate data is not allowed.
# store values in random order
# mutable datatype are not allowed, list, dict, set

set1 = {5, 7, 8, 7, 3.5, 'Hello', (5, 6, 7), True}
print(set1, type(set1))
# {(5, 6, 7), True, 3.5, 5, 'Hello', 7, 8} <class 'set'>

print("#"*50)
####################
# boolean = bolean store values as True or False.
b1 = True
b2 = False
print(b1, type(b1)) # True <class 'bool'>
print(b2, type(b2)) # False <class 'bool'>
a1 = 30
a2 = 40
print(a1 == a2) # False

print("_"*50)
##################### Type data conversion ######################
# string ->  list conversion
str1 = "Hello"
l1 = list(str1) # ['H', 'e', 'l', 'l', 'o']
print(l1)

# string to integer conversion
str2 = "6789"
num = int(str2)
print(num , type(num)) # 6789 <class 'int'>


# integer to string
num1 = 78978789
s1 = str(num1) # 6789 <class 'int'>
print(s1, type(s1), s1[-1]) # 78978789 <class 'str'> 9

####################################
print("#"*50)
# sort() method: this method sort list data in ascending descending order, 
# and modify the original list.
list_h = [5, 7, 8, 9, 2, 3, 1]
list_h.sort()
print("Ascending order :", list_h) # [1, 2, 3, 5, 7, 8, 9]

list_j = [5, 7, 8, 9, 2, 3, 1]
list_j.sort(reverse=True)     
print("Descending order :", list_j) # [9, 8, 7, 5, 3, 2, 1]

#############
# sorted function :  it returns the sorted value in ascending
# in descending order without modifying original list
list_k = [5, 7, 8, 10, 20, 9, 2, 3, 1]
result =  sorted(list_k)
result2 = sorted(list_k, reverse=True)
print("ascending result :", result) # [1, 2, 3, 5, 7, 8, 9, 10, 20]
print("descending result :", result2)  # [20, 10, 9, 8, 7, 5, 3, 2, 1]


list_l = [5, 7, 8, 10, 20, 9, 2, 3,10,20, 1]
result=sorted(list_l)
print("sorted list :", result) # [1, 2, 3, 5, 7, 8, 9, 10, 10, 20, 20]  
result2 = sorted(list_l, reverse=True)
print("sorted list in descending order :", result2) # [20, 20, 10, 10, 9, 8, 7, 5, 3, 2, 1]



