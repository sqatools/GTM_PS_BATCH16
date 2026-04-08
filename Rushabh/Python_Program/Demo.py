# def even_odd_input():
#     no=int(input("Enter number"))

#     if(no%2==0):
#         print("Number is even")
#     else:
#         print("Number is odd")


# even_odd_input()


# def message():
#     print("Hello World")

# message()

# def add(a,b):
#     # a=int(input("Enter first number"))
#     # b=int(input("Enter second number"))
#     c=a+b
#     print(c)

# add(20,30)


t = (1, 2, 3)

# This will raise an error:
# t[0] = 99  → TypeError!

# Workaround: convert to list, edit, convert back
temp = list(t)

temp[0] = 99
t = tuple(temp)
print(t)

# Concatenate to create a new tuple
t2 = t + (4, 5)
print(t2)
