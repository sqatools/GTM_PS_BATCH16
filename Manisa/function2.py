#import specific variable and function
from function1 import var_a,add

print("value of a:", var_a)
result = add(78,99)
print("add", result)

#import everything from function1.py
from function1 import *
print("value of b:", var_b)