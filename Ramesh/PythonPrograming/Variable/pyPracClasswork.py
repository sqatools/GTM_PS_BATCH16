# write a program to get all the people age which are eligible to vote 

list1 = [6,7, 9, 23, 45, 12,68, 24, 18]

for i in list1:
    if i >= 18:
        print ("Eligible to vote")
    else:
        print ("Not eligible for vote")



########

# write a program to square all the value which are divisible by 5 

list2 = [5, 10 , 7 , 23, 12, 5, 7, 35, 45]

for i in list2:
    if i % 5 == 0:
        print("""The numbers are divisible by 5
        Square of the number is """, i**2)
    else:
        pass
