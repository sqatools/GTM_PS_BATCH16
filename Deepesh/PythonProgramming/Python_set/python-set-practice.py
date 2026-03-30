# Python Set
"""
- Set is mutable data type.
- Set can only contains immutable data type as member.
- Set only contains unique value, duplicate values not allowed.
- Set store value in random order.
"""

set1 = {10, 3.4, "Hello", (4, 6, 7), True, None, 10, 3.4, True} 
print(set1, type(set1))
# {None, True, 'Hello', 3.4, (4, 6, 7), 10} <class 'set'>

############# Set Methods ##############
set_a = {'a', 'b', 'c', 5, 6, 7}
set_b = {'p', 'q', 'c', 5, 6, 'a'}

# union of sets
result = set_a.union(set_b)
print("Union result :", result) # {'q', 5, 6, 7, 'b', 'c', 'a', 'p'}

# intersection between sets :  common value between both sets.
result2 = set_a.intersection(set_b)
print("Intersection result :", result2) # {'a', 5, 6, 'c'}


# difference :  get difference between both the sets.
result3 = set_a.difference(set_b)
print("difference result :", result3) # {'b', 7}

result4 = set_b.difference(set_a)
print("difference result :", result4) # {'q', 'p'}

# symmetric difference in both the sets.
result5 = set_a.symmetric_difference(set_b)
print("symmetric difference output :", result5) # {7, 'p', 'b', 'q'}

print("#"*50)
# Add value to set:
set_7 = {'q', 5, 6, 7, 'b', 'c', 'a', 'p'}
print(set_7, type(set_7))

for val in set_7:
    print(val)
"""
5
q
6
b
7
p
c
a
"""

# remove value from set
set_8 = {'q', 5, 6, 7, 'b', 'c', 'a', 'p'}
val = set_8.pop()
print("removed value :", val) # removed value : p
print("set_8:", set_8) # set_8: {5, 6, 7, 'q', 'b', 'c', 'a'}

# remove method :  to remove specific value from set and does not return.
val2 = set_8.remove('b')
print(val2) # None
print("set_8:", set_8) # set_8: {5, 6, 7, 'q', 'a', 'p'}

# remove non exisiting value, it throws error,  like KeyError: 'x'
# set_8.remove("x") # KeyError: 'x'

print("_"*50)
# discard method :  this method remove any value from set and does not return anything.
set_9 = {'q', 5, 6, 7, 'b', 'c', 'a', 'p'}
set_9.discard(7)
print("set_9 :", set_9) # {'a', 5, 6, 'b', 'c', 'q', 'p'}

set_9.discard('y') # does not give erro if value is not there.
print("set_9 :", set_9) # {'a', 5, 6, 'b', 'c', 'q', 'p'}