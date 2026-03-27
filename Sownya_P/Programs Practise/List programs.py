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

## program to differentiate even and odd elements from the given list into a list

list1 = [21,8,154,30,17,200,53,78]
list2 = []
list3 = []
for x in list1:
    if x%2 == 0:
        list2.append(x)
    else:
       list3.append(x)
print("odd and even numbers are", list2, "and ", list3)

print("-"*50)

## program to differentiate even and odd numbers from given list
list1 = [21,8,155,30,17,200,53,78]

for x in list1:
    if x%2 == 0:
        print("even no. : ", x )
    else:
        print("odd number : ", x )


print("-"*50)
## program to remove all duplicate elements from the list.

list1 = [ 2,8,15,30,80,2,16,30,77,80,230]
out1= []
for x in list1:
    if x not in out1:
        out1.append(x)

print(out1)

print("-"*50)

## program to print a combination of 2 elements from the list whose sum is 10.
