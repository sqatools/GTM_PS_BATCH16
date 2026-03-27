# 1. Python program to calculate the square of each number from the given list.

list1 = [1, 2, 3, 4, 5]

for a in list1:
    print(a, ":", a**2)


# 2. Python program to combine two lists.


list2 = [1, 2, 3, 4]
list3 = ['a', 'b', 'c', 'd']

print(list2 + list3)


# 3. Python program to calculate the sum of all elements from a list.

list4 = [1, 2, 3, 4, 5]
sum = 0

for b in list4:
    sum += b

print(sum)


# 4. Python program to find a product of all elements from a given list.

list5 = [1, 2, 3, 4, 5]

mul = 1

for c in list5:
    mul *= c

print(mul)


# 5. Python program to find the minimum and maximum elements from the list.

list6 = [11, 2, 3, 4, 5]
list6.sort()
print(list6[0])
print(list6[-1])


# 6. Python program to differentiate even and odd elements from the given list.

list7 = [1, 2, 3, 4, 5]

even = []
odd = []

for x in list7:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
print(even)
print(odd)


# 7.  Python program to remove all duplicate elements from the list.

list8 = [1, 2, 3, 4, 5, 3, 1]

list9 = []

for value in list8:
    if value not in list9:
        list9.append(value)
    else:
        continue
print(list9)


# 9. Python program to print squares of all even numbers in a list.

list_a = [1, 2, 3, 4, 5, 8]

for value in list_a:
    if value % 2 == 0:
        print(value **2) 
    else:
        continue


# 10. Python program to split the list into two-part, the left side all odd values and the right side all even values.
# Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]

list_b = [5, 7, 2, 8, 11, 12, 17, 19, 22]

even = []
odd = []

for value in list_b:
    if value % 2 ==0:
        even.append(value)
    else:
        odd.append(value)
odd.extend(even)

print(odd)


# 11. Python program to get common elements from two lists.
# Input =
# list1 = [4, 5, 7, 9, 2, 1]
# list2 = [2, 5, 8, 3, 4, 7]

list_c = [4, 5, 7, 9, 2, 1]
list_d = [2, 5, 8, 3, 4, 7]

common_list = []

for value in list_c:
    if value in list_d:
        common_list.append(value)
    else:
        continue

print(common_list)

