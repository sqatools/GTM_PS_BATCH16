#Create a list of numbers from 1 to 10 and print it.
from tokenize import String

l1 = [1,2,3,4,5,6,7,8,9,10]
print(l1)
l2 = []
for i in range(1,11):
    l2.append(i)
    print(l2)
print(l2)

#Access the first and last element of a list.
print(l1[0],l1[-1])
#	3.	Append a new item to a list.
l1.append(11)
print(l1)
#	4.	Remove an item from a list.
l1.pop() # last value
l1.remove(10)
l1.pop(5)

#11.	Write a program to find the second largest number in a list.
l10 = [1,4,5,6,7,8,9,10,3,7,5,2]
l10.sort()
print(l10,l10[-2])

#Python program to calculate the square of each number from the given list.
sqLst = [1,2,3]
for i in sqLst:
    print("square:",i*i)
#Python program to combine two lists.
L100 = [1,2,3]
L101 = [4,5,6]
L100.extend(L101)
print(L100)
#Python program to calculate the sum of all elements from a list.
sumLst = [1,4,5,6,7,8,9,10,3,7,5,2]
print(sum(sumLst))
#Python program to find a product of all elements from a given list.
sumLst = [1,4,5,6,7,8,9,10,3,7,5,2]
pr = 1
for i in sumLst:
    pr *= i
print(pr)
#Python program to find the minimum and maximum elements from the list.
minMaxLst = [1,4,5,6,7,8,9,10,3,7,5,2]
print(min(minMaxLst), max(minMaxLst))

#Python program to differentiate even and odd elements from the given list.
evnOddLst = [1,4,5,6,7,8,9,10,3,7,5,2]
print([val for val in evnOddLst if val%2 == 0])
print([val for val in evnOddLst if val%2 == 1])

print(dir(list))
print(dir(tuple))
print(dir(str))













