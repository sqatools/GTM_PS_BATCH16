"""
1. Number
    i)int
    ii)float

2. String / Sequential
     i)string
     ii)list
     iii)tuple

3. dictionary
4. Set
5. Boolean
 
"""

# 1. Number / Integer
a = 10
print(a, type(a))

# 2. Number / Float
b = 10.5
print(b, type(b))

# 3. String
c = "Hello, World!"
a = 'python'
b ='''we are learning python'''
d = """python is a great language"""
print(c, type(c))
print(a, type(a))
print(b, type(b))
print(d, type(d))

#indexing
print(a[3])  # h
print(b[3])  # a
print(c[-3])  # l
print(d[0])  # p


# 4. List - can be modified (mutable)
d = [1, 2, 3, 4, 5]
print(d, type(d))

l1 = [1, 2.5, "hello", [1, 2], (3, 4), {"name": "Alice"}, {1, 2, 3}]
print(l1, type(l1))
print(l1[2])  # "hello"
print(l1[3])  # [1, 2]
print(l1[3][1])  # 2
print(l1[4])  # (3, 4)

# 5. Tuple - cannot be modified (immutable)
e = (1, 2, 3, 4, 5)
print(e, type(e))

tup1 = (1, 2.5, "hello", [1, 2], (3, 4), {"name": "Alice"}, {1, 2, 3})
print(tup1, type(tup1))



# 6. 
# Dictionary - store key-value pairs
# keys must be unique and immutable (string, number, tuple)
# values can be of any type and can be duplicated / mutuable

f = {"name": "Alice", "age": 30}
print(f, type(f))

# 7. Set
g = {1, 2, 3, 4, 5}
print(g, type(g))

# 8. Boolean
h = True
print(h, type(h))