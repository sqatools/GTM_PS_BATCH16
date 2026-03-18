##Data Types in Python

a= 10
b= 2051234567890098765432112345678900987654321

c = -23567
print("value of a is", a)
print("value of b is", b) 
print("value of c is", c) 

print(type(a))

print(type(b))

print("-"*50)
d = 3.14
a2 =0.0
print("value of d is", d)
print("value of a2 is", a2)

print("-"*50)
S1 = "Hello World"
S2 = 'Python Programming'
s3 = """This is a multi-line string"""

print("value of S1 is", S1)
print("value of S2 is", S2)
print("value of s3 is", s3)

print(type(S1))

print(S1[8])

print(S2[-4])
print("-"*50)

#list data type - we can declare any type of data type in list and it is ordered and mutable

l1= [13 , 3.14, "Hello", [1,2,3], (4,5,6), {7: "Seven", 8: "Eight"}, True]

print("value of l1 is", l1)

print(l1[2])

print(l1[3][1])

l1.append("new element")
print("value of l1 after append is", l1)

print("-"*50)

# tuple data type - we can declare any type of data type in tuple and immutable

t1 = (13, 3.14, "Hello", [1,2,3], (4,5,6), {7: "Seven", 8: "Eight"}, True)

print("value of t1 is", t1)

print(t1[2])

# t1[2] = "New Value"  # This will raise an error as tuples are immutable



# dictonary data type - it is a collection of key-value pairs and mutable

d1 = {"Name": "John", "Age": 30, "City": "New York"}

print("value of d1 is", d1)

print(d1["Name"])

d1["Age"] = 31

print("value of d1 after update is", d1)

####  d2 = { 12 : 3.14 ,  5.7: "Hello", (1,2): {"a":"t"}, {"key": "value"}: "Dictionary as Key",
###           True : [1,2,3] , 12: "Duplicate Key"}


##   print("value of d2 is", d2)

# print(d2[12])  # This will print "Duplicate Key" as the key 12 is duplicated and the last value will be considered.

 # print(d2[5.7])

# print(d2[(1,2)])


dict2 = {
    23 : 5.6,
    4.5 : "Hello",
    "Python" : [6, 7, 8],
    (5, 7, 8) : {'P': 789, 'Q': 45, 'R': 123},
    True : (4, 5, 67),
    23 : 500
}

print(dict2)
print(dict2["Python"])
print(dict2[(5, 7, 8)]) 
print(dict2.keys())
print(list(dict2.keys())[3][1]) 


