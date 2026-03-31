# Python Set 

"""
- Set is a mutable data type.
- Set can only Contains immutable data type as member.
- Set only contains unique value, duplicate value not allowed .
- Set store value in random order.

"""

set1 = {10, 3.4, "Hello", (4, 6, 7), True, None, 10, 3.4, True}
print(set1, type(set1))

#################### Set Methods ########################

set_a = {'a', 'b', 'c', 5, 6, 7}
set_b = {'p', 'q', 'c', 5, 6, 'a'}
result =set_a.union(set_b)
print(result) #{5, 6, 7, 'a', 'c', 'b', 'p', 'q'}


# Intersection between Sets

result2 = set_a.intersection(set_b)
print(result2) # {'c', 'a', 5, 6}

# defference : get difference between both the sets
result3 = set_a.difference(set_b)
print(result3) # {'b', 7}

result4 = set_b.difference(set_a)
print(result4) # {'q', 'p'}

# Symetric Difference in both the sets.

result5 = set_a.symmetric_difference(set_b)
print(result5) # {'b', 'p', 7, 'q'}

 # Add value to set :
 
set_7 = {'q', 5, 6, 7, 'b', 'c', 'a', 'p'}
print(set_7, type(set_7))

for val in set_7:
    print(val)



# remove value from set 

set_8 = {'q', 5, 6, 7, 'b', 'c', 'a', 'p'}
val = set_8.pop()
print(val)
print(set_8)

# remove method : to remove specific value from set and does not return.

val2 = set_8.remove('b')
print(val2)
print(set_8)

# discard method : this remove any specific value from set and does not return anything.

set_9 = {'q', 5, 6, 7, 'b', 'c', 'a', 'p'}
set_9.discard(7)
print(set_9)

set_9.discard('y')
print(set_9)

