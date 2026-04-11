"""
global variable : 
               ->  When we declare a variable outside of the function, than it is called global variable
               ->  We can use global variable across the fuction in the file or outside of the file.


local variable:
                ->  When we declare variable inside the function, then it is called local variable.
                ->  local variable scope is limited to the function, can not use outside of the function.

non local variable:
                -> non local variable are accessible for all the inner function, can not access outside of outer function.
                -> If we want to change the value of global or non local variable we have to use the keyword, global, nonlocal
"""

# global variable
var_x = 50

def function1():
    # local variable
    var_y = 60
    print("global variable var_x:", var_x)
    print("local variable  var_y:", var_y)


function1()
# can not access local variable outside of function.
# print("var_y :", var_y)


# global variable
var_p = 100

def outer_function():
    # non local variable
    var_q = 200

    def inner_function1():
        # local variable
        global var_p
        var_p = 700
        var_r = 300
        print("global variable var_p :", var_p)
        print("non local variable var_q:", var_q)
        print("local variable var_r:", var_r)

    
    def inner_function2():
        # local variable
        nonlocal var_q
        var_q = 500
        print("global variable var_p :", var_p)
        print("non local variable var_q:", var_q)
        # can not access local variable in another inner function
        #print("local variable var_r:", var_r)

    inner_function2()
    print("--"*10)
    inner_function1()
    print("--"*10)
    inner_function2()


outer_function()