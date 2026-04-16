"""
-> list is mutable data type, user can modify and update it.
-> List can contain all types of data.
-> List Follows +ve and -ve Indexing as like string.
"""

# message = "Welcome to GeeksforGeeks"
# msg = message.replace("W","P")
# print(msg)
# print(message)
#
# my_list = [1, 2, 3]
# my_list.append(4) #[1, 2, 3, 4]
# print(my_list)
#
# my_list.insert(1, 5) #[1, 5, 2, 3, 4]
# print(my_list)
#
# my_list.remove(5)#[1, 2, 3, 4]
# print(my_list)
#
# popped_element = my_list.pop(0) #[2, 3, 4]
# print(my_list)
# print(popped_element) #1

list1 = [2, 3.5, 'Hello', [4, 6, 7], (2, 1, 3), {'a':123}, {5, 6, 7}, True]
print(list1, type(list1))
# [2, 3.5, 'Hello', [4, 6, 7], (2, 1, 3), {'a': 123}, {5, 6, 7}, True] <class 'list'>

# get value with +ve indexing
print(list1[2])
# Hello

print(list1[3]) # [4, 6, 7]
print(list1[3][1]) # 6

print(list1[-2]) # {5, 6, 7}


########## slicing in the list #############
list2 = [2, 3.5, 'Hello', [4, 6, 7], (2, 1, 3), {'a':123}, {5, 6, 7}, True]
print(list2[0:4])  # [2, 3.5, 'Hello', [4, 6, 7]]

print(list2[-1:-5:-1]) # [True, {5, 6, 7}, {'a': 123}, (2, 1, 3)]

print(list2[::-1]) # [True, {5, 6, 7}, {'a': 123}, (2, 1, 3), [4, 6, 7], 'Hello', 3.5, 2]

print("#"*50)
##########  List Methods ############
# append() method : Add value at the end of list
l1 = [5, 6, 7, 8]
l1.append(100)
l1.append("Python")
print("l1 :", l1) # l1 : [5, 6, 7, 8, 100, 'Python']

print("#"*50)
# insert() method : Add value at specific index position.
l2 = [5, 6, 7, 8, 10, 13, 15]
l2.insert(2, 500)
print(l2) # [5, 6, 500, 7, 8, 10, 13, 15]


print("#"*50)
# extend() method : This method help to add one list data to another list.
l4 = [5, 6, 7]
l5 = ['a', 'b', 'c']
l5.extend(l4)
print("l5 :", l5) # ['a', 'b', 'c', 5, 6, 7]

print("#"*50)
# list concatenation
list_a = [5, 6, 7]
list_b = ['a', 'b', 'c']
list_c = list_a + list_b
print("list_c :", list_c) #  [5, 6, 7, 'a', 'b', 'c']
print("list_b :", list_b)
list_b = list_a + list_b
print("list_b :", list_b) # [5, 6, 7, 'a', 'b', 'c']


print("#"*50)
# remove method : remove any specific value from list
list_d = [5, 6, 7, 8, 4, 15]
list_d.remove(15)
print("list_d :", list_d) # [5, 6, 7, 8, 4]

print("#"*50)
# pop method : this method remove from specific index. default index is -1
list_e = ['a', 'b', 4, 5, 6, 7, 8]
val = list_e.pop()
print("removed value :", val) # removed value : 8

val1 = list_e.pop(2)
print("removed value :", val1) # removed value : 4

print(list_e) # ['a', 'b', 5, 6, 7]

# clear all data from list using clear method.
list_e.clear()
print("list_e :", list_e) # list_e : []

####################################
print("#"*50)
# reverse() method: this method reverse all the list value and modify original list
list_g = [5, 7, 8, 9, 2, 3]
list_g.reverse()
print("list_g :", list_g) # [3, 2, 9, 8, 7, 5]


list_f = [5, 7, 8, 9, 2, 3, 'a', 'b']
print(reversed(list_f))
result = list(reversed(list_f))
print("reversed result :", result) # ['b', 'a', 3, 2, 9, 8, 7, 5]


####################################
print("#"*50)
# sort() method: this method sort list data in ascending descending order,
# and modify the original list.
list_h = [5, 7, 8, 9, 2, 3, 1]
list_h.sort()
print("Ascending order :", list_h) # [1, 2, 3, 5, 7, 8, 9]


list_j = [5, 7, 8, 9, 2, 3, 1]
list_j.sort(reverse=True)
print("Descending order :", list_j) # [9, 8, 7, 5, 3, 2, 1]

#############
# sorted function :  it returns the sorted value in ascending
# in descending order without modifying original list
list_k = [5, 7, 8, 10, 20, 9, 2, 3, 1]
result =  sorted(list_k)
result2 = sorted(list_k, reverse=True)
print("ascending result :", result) # [1, 2, 3, 5, 7, 8, 9, 10, 20]
print("descending result :", result2)  # [20, 10, 9, 8, 7, 5, 3, 2, 1]