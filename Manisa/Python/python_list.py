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


#1). Python program to calculate the square of each number from the given list.

list1 = [1, 2, 3, 4, 5]
squared_list = []
for num in list1:
    squared_list.append(num **2)
#squared_list = [num ** 2 for num in list1]#advanced way to calculate square of each number from the list
print("sqaure_list-", squared_list)

#2. Problem to add elements from list1 to list2

list1 = [4, 9, 6, 7, 8]

list2 = [8, 5, 6, 8]

#list2.append(list1)
list3 = list1+list2

print(list3)

for a in list1:
    list2.append(a)

print(list2)

#3). Python program to calculate the sum of all elements from a list.

list_s = [1,8,9,84,45]

sum = 0

for a in list_s:
    sum = sum + a

print(sum)

list1 = [1,2,41,3]

print(list1)
#print(sum(list1))


#4). Python program to find a product of all elements from a given list.

list1 = [2, 5, 7, 8]

product = 1

for p in list1:
    product = product*p

print(product)

#5). Python program to find the largest and smallest number from a given list.

list1 = [9, 2, 11, 7, 8]

list1.sort()

print(list1)

print("largest element - ", list1[0])
length_list = len(list1)
print(length_list)

print("smallest element - ", list1[length_list-1])

print(max(list1))
print(min(list1))


list_2 = [22, 45, 66, 11, 43]

odd_list = []
even_list = []

for a in list_2:
    if a%2 == 0:
        print(a ,"is a even number")
        even_list.append(a)
    else:
        print(a, "is a odd number")
        odd_list.append(a)
print("even_list :", even_list)
print("odd_list :", odd_list)

#program to remove all duplicate elements from the list

list_y = [1, 6, 8, 88, 9, 88, 9, 2, 22, 23, 25, 6]

list_u = []

for a in list_y:
    if a not in list_u:
        list_u.append(a)
print("unique list value :", list_u)




