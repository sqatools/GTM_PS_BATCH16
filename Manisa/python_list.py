"""
list is mutuable datatype, user can modify and update it
list can contain all types of data
list follows +ve and -ve indexing as string


"""

list1 =[2, 3.5, 'hello', [2,3,5], (1, 2, 3), {'a':123}, {2, 6, 7}, True]

#+ve indexing
print(list1[3])

print(list1) #entire list 

print(list1[3]) #third element

print(list1[3][0]) #child element from third element from the 

#slicing of list
print(list1[0:4])

print(list1[-1:-5:-2])

print(list1[::-1]) #reverse the list

#list methods
l1 = [5, 6, 7, 9, 10]
l1.append(100)
l1.append("python")

print(l1)

#insert method at specific index position
l2 = [2, 6, 7]
l2.insert(2, 500)
print(l2)


#extend method add one list data to another list
l4 = [3, 5, 9]

l5 = ['a', 'b', 'c']

l5.extend(l4)
print(l5)

#concantenation
l6 = l5+l4

print(l6)

#remove any specific value from list
l6.remove('b')
print(l6)
val = l6.pop(4)
print(l6) #remove value from 4th position

l6.clear() #clear the list
print("print l6-", l6)

list_a = ['l', 'n', 'm', 'o', 'p', 8, 9]
list_a.reverse() #reverse the list
print(list_a)

#not reversing the actual list but showing the result in reverse
list_b = [5, 2, 3, 4]
result_list = list(reversed(list_b)) 
print(result_list)

#sort method, modified the list
list_b.sort()
print("ascending order list", list_b)
list_b.sort(reverse=True)
print("descending order list-", list_b)

#without modifying original list
list_b = [5, 2, 3, 4]
result = sorted(list_b)
result1 = sorted(list_b, reverse = True)
print(result)
print(result1)
