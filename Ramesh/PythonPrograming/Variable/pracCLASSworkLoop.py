#  write a python loops program to find those numbers which are divisible by 7 and multiple of 5 , between 1500 and 2700(both included)

for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)



#####################################

# python loops program to count the number of evevn and odd numbers from a serie of numbers using pythoon.


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_count = 0
odd_count = 0

for i in list1:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    print("Number of even numbers:")
    print("Number of odd numbers:")




###################################


# write a program that prints all the numbers from 0 to 6 except 3 and 6 using python


for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i)




###################################


# python loops program to construct the following pattern, using a nested for loops 


for i in range(1, 6):
    for j in range(i):
        print(" * ", end="")
    print()