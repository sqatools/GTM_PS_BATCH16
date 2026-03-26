tup1 = (4, 4.5, 'Hello', [5, 6, 7], (1, 2, 3), {'a' : 345}, { 6, 7, 8}, True)
print(type(tup1))

print(tup1[2])
print(tup1[3][2])


# slicing on tuple
print(tup1[0:4])

print(dir(tup1))

tup3 = (4, 5, 6, 7, 4, 5, 6, 23, 12, 4)

print(tup3.count(4))
print(tup3.index(23))

print(max(tup3))
print(min(tup3))
print(sum(tup3))

tup4 = ('a', 2, 4, 'Hello', 'Python', 'a', 'b', 'c', 'a')


# write a python program to remove all the duplicate values from tuple.


tup_1 = (4, 5, 6, 7, 4, 5, 2, 5, 6, 1)

list1 = []

for value in tup_1:
    if value not in list1:
        list1.append(value)
    else:
        continue
print(list1)

result = []
[result.append(value) for value in tup_1 if value not in result]
print(result)