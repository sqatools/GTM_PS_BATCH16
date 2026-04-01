#global variable
vari_g=50

def function1():
    #local variable
    vari_l=60
    print("Local variable--->",vari_l)
    print("Global variable--->",vari_g)

function1()
#print("local variable calling outside of function-->",vari_l)

print("*"*30)
var_p=100 # global variable 
def outer_fun():
    var_q=200 # q is local for outer fun but non local for inner fun
    def inner_fun():
        var_r=300 # r is local to inner fun only 
        print("Global variable vari_p",var_p)
        print("non local variable var_q",var_q)
        print("local variable var_r",var_r)
    inner_fun()

outer_fun()       




