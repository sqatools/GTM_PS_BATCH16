#1). Python program to calculate the square of each number from the given list.
list1 = [1, 2, 3, 4, 5]
for i in list1:
    print(i**2)             

#combine two list
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
combine_list = list1 + list2   
print(combine_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#sum of all the numbers in the list
list1 = [1, 2, 3, 4, 5]
Sum_all = sum(list1)
print(Sum_all) # 15

#find a product of all elements from a given list.

list_product = [1, 2, 3, 4, 5]

var = 1

for value in list_product:
    var *= value

print(var)

############
list1 = [23,56,12,89]

print("Smallest number: ", min(list1))
print("Largest number: ", max(list1))