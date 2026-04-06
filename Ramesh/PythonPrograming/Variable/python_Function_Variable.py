"""
global variable 
            -> when we declare a variable outside of the fumction , then it is called global variable
            -> we can use variable across the function in the file oroutside of the file.


 local variable:
                -> when we declare variable inside the function than it it called local variable.
                -> local variable scope is limited to the function, can not use outside of the fumction.
non local variable:
                -> non local variables are accessible for all the inner function, can not acces outside of outer function.
                -> If we want to change the value for global or non locval variable we have to use the keyword, gloabal, non local
"""
# global variable
var_x = 50

def function1():
    # local variable
    var_y = 60
    print(var_x)
    print(var_y)

function1()
# can not acces local variable outside of the function.
# print(var_y)


# global variable
var_p = 100

def outer_function():
    var_q = 200

    def inner_function():
        var_r = 300
        print(var_p)
        print(var_q)
        print(var_r)
    
    def inner_function2():
        print(var_p)
        print(var_q)
        # print(var_r)
    
    inner_function()
    inner_function2()

outer_function()