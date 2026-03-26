tup1 = (4, 4.5, 'Hello', [5, 6, 7], (1, 2, 3), {'a': 345}, {6, 7, 8}, True)
print(tup1, type(tup1))

# (4, 4.5, 'Hello', [5, 6, 7], (1, 2, 3), {'a': 345}, {8, 6, 7}, True) <class 'tuple'>

print(tup1[3]) # [5, 6, 7]
print(tup1[3][1]) # 6


# splicing on tuple
print(tup1[0:4]) # (4, 4.5, 'Hello', [5, 6, 7])
print(tup1[::-1]) # (True, {8, 6, 7}, {'a': 345}, (1, 2, 3), [5, 6, 7], 'Hello', 4.5, 4)

print(dir(tup1)) # 'count', 'index'

tup3 = (4, 5, 6, 7, 4, 5, 6, 23, 12, 4)
print("count of 4 :", tup3.count(4)) # count of 4 : 3
print("index of 23:", tup3.index(23)) # index of 23: 7
print("max value :", max(tup3)) # max value : 23
print("min value:", min(tup3)) # min value: 4
print("sum of values :", sum(tup3)) # sum of values : 76

tup4 = ('a', 2, 4, 'Hello', 'Python', 'a', 'b', 'c', 'a')