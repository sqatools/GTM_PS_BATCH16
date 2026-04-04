from function_file1 import var_A, addition
#from function_file1 import var_B, substraction
print("Calling variable A in other file ", var_A)
result=addition(500,500)
print("Addition of variables ",result)
#print("Calling variable B in other file", var_B)

#import all variables and functions in single line

from function_file1 import *
print("Calling variable B in other function using import all ", var_B)
print("Calling subtraction method using import all ", substraction(500,300))

