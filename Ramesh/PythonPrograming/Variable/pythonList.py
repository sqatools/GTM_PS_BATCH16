"""
-> list is mutable data type.
-> list can contain all types of data..
-> list follows +ve and -ve Indexing. as like string..

"""

list1= [2, 3.5, 'Hello', [4, 6, 7], (2, 1, 3), {'a' : 123}, {5, 6, 7}, True]
print(list1, type(list1))

#get value with +ve indexing 
print(list1[2])

print(list1[3][1])
print(list1[-2])


############ Slicing in the list #######################

list2 = [2, 3.5, 'Hello', [4, 6, 7], (2, 1, 3), {'a' : 123}, {5, 6, 7}, True]
print(list2[-1:-5:-1]) 
print(list2[::-1])

############  List methods #######################
# append method : Add value at the end of list.

l1 = [5, 6, 7, 8]
l1.append(100)
l1.append("Python")
print(l1)

# insert() method : add value at specific index positio.

l2 = [5, 6, 7, 8, 9, 10, 11, 12]
l2.insert(3, 500)
print(l2)


# extend() method : this method help to add list data to another list .

l4 = [5, 6, 7, 8]
l5 = ['a', 'b', 'c', 'd']
l5.extend(l4)
print(l5)

# list concatenation 

list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']
print(list_a + list_b)

# list remove() : remove any specific value from list 

list_d = [5, 6, 7, 8, 4, 15]
list_d.remove(7)
print(list_d)

# pop method : this method remove from specific index default index is -1

list_e = ['a', 'b', 4, 5, 6, 7, 8]
val = list_e.pop()
val2 = list_e.pop(1)
print(val)
print(val2)

# clear methods : clear all data from list using clear method.

list_e.clear()
print(list_e)

####################################

# reverse() method : 

list_d = [5, 6, 7, 8, 4, 15]
list_d.reverse()
print(list_d)

# sort () method : thios method sort list in ascendeing and descending order, and modify the original list.

list_h = [5, 7, 8, 9, 2, 3, 1]
list_h.sort()
print("Ascending order :",list_h)

list_i = [5, 7, 8, 9, 2, 3, 1]
list_i.sort(reverse=True)
print("Descending oder :",list_i)

list_j = [5,7,8,20, 9, 2, 3, 1]
result = sorted(list_j)
result2 = sorted(list_j, reverse = True)
print(result)
print(result2)
