# program to calculate the square of each number from the given list

list1 = [ 2,8,15,30,80,200]
for x in list1:
    print("square of each number in the list :", x**2 )

## Python program to combine two lists.
list2 = [ 12, 454, 16, 29]
list3 = list1 + list2
print(list3)

list4 = [ 15, "a", 'hello']
list5 = list2+list4
print(list5)

## program to calculate the sum of all elements from a list.
list1 = [ 2,8,15,30,80,200]
print (" sum of elements of the list: ", sum(list1))

## program
sum = 0
for x in list1:
    sum = sum + x
print(sum)

# program to find a product of all elements from a given list.
list1 = [ 2,8,15,30,80,200]
product =1
for x in list1:
    product = product * x
print("product of elements in the list ", product)

#program to find the minimum and maximum elements from the list using methods

print(max(list1))
print(min(list1))

print("-"*50)
## program to find the minimum and maximum elements from the list.
list1 = [22,8,15234,30,18,200]

min1 = list1[0]
max1 = list1[0]
for x in list1:
    if x < min1:
        min1 = x
    if x > max1:
        max1 = x
print("min and max values are", min1, "and ", max1 )

