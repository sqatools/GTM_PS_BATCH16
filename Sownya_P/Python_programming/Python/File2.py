

var3= 40
from function_file1 import var1, var2, subtraction #importing variables and function from another file

#from function_file1 import * #importing all functions from another file

def multiplication(n1, n2):
    print("multiplication of values :", n1*n2)  

res1 =subtraction(var1,var2)  ## calling function from another file
res2 = multiplication(var1,var3)  ## calling function from same file

print("*"*50)
print("Result 1:", res1)
print("Result 2:", res2)
