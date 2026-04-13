from unicodedata import name


dict1 = {'a': 123, 'b': 456, 'c': 789, 'd': 123, 'e': 456, 'f': 789}

for data in dict1:
    print(data, dict1[data])  # prints the keys and values of the dictionary


print(dict1.items())  # prints the items of the dictionary as a list of tuples


p, q = (100, 200)  # unpacking the tuple into variables p and q
print(p, q)

for k, v in dict1.items():  # unpacking the items of the dictionary into key and value
    print(k, v, end=" ,")  # prints the keys and values of the dictionary

print("_"*50)
for i in range(1, 20):
    if i % 2 == 0:
        print(i, end=" ,")  # prints the even numbers from 1 to 20
    else:
        pass

print("\n"+"_"*50)
for i in range(1, 10):
    if i in [4, 6, 7, 8]:
        pass
    print(i)


print("\n"+"_"*50)
for i in range(1, 10):
    if i in [4, 6, 7, 8]:
        continue
    print(i)


if -1: # -1 is a truthy value, so this block will execute
    print("This is a truthy value")

if 0: # 0 is a falsy value, so this block will not execute
    print("This is a falsy value")
else:
    print("This is a falsy value")


# lambda function: It is an anonymous function, which can have any number of arguments but only one expression. The expression is evaluated and returned.
# syntax: lambda arguments: expression

result = lambda x: x**2  # lambda function to calculate the square of a number
print(result(5))  # prints the square of 5

result2 = lambda x: x**2 if x %2 == 0 else x**3  
# lambda function to calculate the square of a number if it is even, otherwise calculate the cube
print(result2(4))  # prints the square of 4
print(result2(5))  # prints the cube of 5


str1 = "RAMESH"
print(str1[-2::-1]) # SEMAR

name = "Deepesh"
_name = "Rahul"
__name = "Suresh"
print(name) # Deepesh
print(_name) # Rahul
print(__name) # Suresh


# set comprehension: It is a concise way to create a set. 
# It consists of an expression followed by a for clause, then zero or more for or if clauses.
set1 = {i**2 for i in range(1, 11) if i % 2 == 0} 
# set comprehension to create a set of squares of even numbers from 1 to 10
print(set1) # {64, 4, 16, 36, 100}

y = [1, 2, 3, 4, 5]
result = {x**2 for x in y}
print(result)  # {1, 4, 9, 16, 25}

# tuple comprehension: It is a concise way to create a tuple.
tupresult = tuple(i**2 for i in range(1, 10) if i % 2 == 0)
print(tupresult)  # <generator object <genexpr> at 0x7f8c8c8c8c8c>
# (4, 16, 36, 64)


# frozenset
frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)  # frozenset({1, 2, 3, 4, 5})