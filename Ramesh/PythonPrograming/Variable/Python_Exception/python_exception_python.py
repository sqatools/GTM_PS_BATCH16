def calculate(n1, n2):
    try:
        # n1 = 40
        # n2 = "Python"
        addition = n1 + n2
        print(addition)

    except Exception as e:
        print(f"Exception error: {e}")
        print("can not addd number with string.")

calculate(1, 2)
print("Calculation is completed")

print("__"*20)
# try-except-else condition

def try_except_else(n1, n2):
    try:
        # n1 = 40
        # n2 = "Python"
        addition = n1 + n2
        print(addition)

    except Exception as e:
        print(f"Exception error: {e}")
        print("can not addd number with string.")
    else:
        # else section will only executes when there is no exception.
        print("Operation succesfull")

try_except_else(20, 40)


# try-excepte-else-finally

def try_except_else(n1, n2, n3):
    try:
        # n1 = 40
        # n2 = "Python"
        addition = n1 + n2
        print(addition)

    except Exception as e:
        print(f"Exception error: {e}")
        print("can not addd number with string.")
    else:
        # else section will only executes when there is no exception.
        print("Operation succesfull")
    finally:
        # finally block alway going to excutes, even there is exception or no exception
        for i in range(1, 11):
            print(n3, "*", i, ":", i*n3)

try_except_else(10, "Hello", 4)

print("___"*20)

################################################
# Handle multiple exceptions

def try_handle_multiple_exception(n1, n2, n3, n4):
    try:
        add = n1+n2
        print(add)
        print("--"*5)
        assert n2  == n3, "both numbers are not equal"
        print(n3/n4)
    except TypeError as t1:
        print(t1)
        print("Cannot add number with string")
    except ValueError as v1:
        print(v1)
        print("cannot add number and string")
    except AssertionError as v2:
        print(v2)
        print("Compraision failed both the numbers") 
    except ZeroDivisionError as v3:
        print(v3)
        print("Cannot divide number with zero")   
    except Exception as e:
        print(e)
        raise

try_handle_multiple_exception(5, 12, 4, 6)