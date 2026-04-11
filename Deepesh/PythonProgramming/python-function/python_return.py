def add():
    return 10
add()
print("without storing value in variable function called inside print",add())

# if we write return method then its mandatory to store return value in variable

def add():
    return 500
x=add()
print("with storing value in variable x function called ",x)

#we can return multiple values with return statement and store it in single variable.we get o/p in tuple format
def calculator():
    return 10+10,10*100,10%10,500-500
y=calculator()
print("Multiple values are stored in single variable ",y)

#same program with multiple variables

def calculator1():
    return 10+10,10*100,10%10,500-500
a,b,c,d=calculator1()
print("Multiple values stored in multiple variables",a,b,c,d)

def calculator1():
    return 10+10,10*100,10%10,500-500
a,b,c,d=calculator1()
print("Multiple values stored in multiple variables",a,b,c)



s = "hello world  "
res = s.count(" ")
print(res)


s = '  **#Geeks for Geeks '
res = s.strip()
print(res)

s = "Pythonabc"

# Reverse the string
print(s[::-2])