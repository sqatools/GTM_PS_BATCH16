
def calculate(n1, n2):
    try:
        addition = n1+n2
        print("Addition is :", addition)
    except Exception as e:
        print(f"Exception error :{e}")
        print("Can not add number with string.")


# calculate(10, 20)
# print("Calculation is completed")
# Addition is : 30
# Calculation is completed

#calculate(10, 'Python')
#print("Calculation is completed")
# Exception error :unsupported operand type(s) for +: 'int' and 'str'
# Can not add number with string.
# Calculation is completed




##################################################
# try-except-else condition

def try_except_else(n1, n2):
    try:
        addition = n1+n2
        print("Addition is :", addition)
    except Exception as e:
        print(f"Exception error :{e}")
        print("Can not add number with string.")
    else:
        # else section will only executes when there is no exception.
        print("Operation successful")


"""
try_except_else(20, 40)
Addition is : 60
Operation successful
"""

"""
try_except_else(20, 'H')
Exception error :unsupported operand type(s) for +: 'int' and 'str'
Can not add number with string.
"""


# try-except-else-finally condition

def try_except_else(n1, n2, n3):
    try:
        addition = n1+n2
        print("Addition is :", addition)
    except Exception as e:
        print(f"Exception error :{e}")
        print("Can not add number with string.")
    else:
        # else section will only executes when there is no exception.
        print("Operation successful")
    finally:
        # finally block alway going to executes, even there is exeception or no exception
        print("finally block")
        for i in range(1, 11):
            print(i,"*", n3, ":", i*n3)


try_except_else(10, 'Hello', 5)
"""
Exception error :unsupported operand type(s) for +: 'int' and 'str'
Can not add number with string.
finally block
1 * 5 : 5
2 * 5 : 10
3 * 5 : 15
4 * 5 : 20
5 * 5 : 25
6 * 5 : 30
7 * 5 : 35
8 * 5 : 40
9 * 5 : 45
10 * 5 : 50
"""

###############################
# Handle multiple exceptions
def try_handle_multiple_exception(n1, n2, n3, n4):
    try:
        add = n1+n2
        print("addition :", add)
        assert n2 == n3, "both numbers are not equal"
        print("division :", n3/n4)
    except TypeError as t1:
        print(t1)
        print("Can not add number with string")
    except ValueError as v1:
        print(v1)
        print("valus are not correct")
    except AssertionError as v2:
        print(v2)
        print("Comparision failed both the numbers")
    except ZeroDivisionError as v3:
        print(v3)
        print("Can not divide number with zero")
    except Exception as e:
        print(e)
        raise

try_handle_multiple_exception(5, 10, 4, 6)