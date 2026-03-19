# range(start, end, step)
# range output will include start value and exclude the end value.

for i in range(1, 10, 2):
    print(i)

"""
1
3
5
7
9
"""
print("#"*50)
# default start value is zero and step value is 1
for i in range(5):
    print(i)

"""
0
1
2
3
4
"""



print("#"*50)
# default step value is 1
# range(2, 7, 1)
for i in range(2, 7):
    print(i)

"""
2
3
4
5
6
"""

print("#"*50)
# get all numbers which are divisible by 3 and 5 from 1 to 100.
for j in range(1, 100):
    if j%3 == 0 and j%5 == 0:
        print(j)
    else:
        pass

"""
30
45
60
75
90
"""

print("#"*50)
for j in range(1, 31):
    if j%3 == 0:
        print("can divide by 3:", j)
        if j%5 == 0:
            print("This number can divide by 5 :", j)
        else:
            pass
    else:
        pass


print("#"*50)
# apply loop list values
list1 = [50, 60, 3, 5, 7]
for val in list1:
    print(val)


print("#"*50)
# apply loop string values
str1 = "Python"
for char in str1:
    print(char)


print("#"*50)
# program to add all the values in the list
list1 = [50, 60, 3, 5, 7, 10, 23]
sum = 0
for val in list1:
   sum = sum + val

print("sum of all values :", sum)

# write a program to get all people age which are eligible to vote
list1 = [6, 7, 9, 23, 45, 12, 68, 24, 18]


# write a program to square all the value which are divisible by 5
list2 = [5, 10, 7, 23, 12, 5, 7, 35, 45]