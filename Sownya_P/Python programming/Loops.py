## for loop ##

for i in range(1,11,1):
    print(i)

print("*"*50)
## default intializer as 0 and step as 1 

for i in range(5):
    print(i)

print("*"*50)

## for loop without intializer

for i in range(0,11,2): 
    print(i)    

## nested loop 

for i in range(1,4):
    for j in range(1,4):
        print(i,j)  

## apply loop on list values
l1 = [10,20,30,40,50]
for i in l1:
    print(i)

print("*"*50)

## apply loop on string values  
s1 = "Python"
for i in s1:    
    print(i)

print("*"*50)
## program to add alla values in the list 

l2 = [10,20,30,40,50]
sum = 0         
for i in l2:
    sum = sum + i
print("Sum of all values in the list:", sum)

print("*"*50)


## program to get all the people age which are eligible to vote
list1 = [6, 7, 9, 23, 45, 12, 68, 24, 18]
for i in list1:
    if i >= 18:
        print(i, "is eligible to vote")

print("*"*50)

## write a program to square all the value which are divisible by 5

list2 = [5,10,7,23,12,5,7,35,45]
for i in list2:
    if i % 5 == 0:
        print("The square of the number which is divisible by 5 is: ", i**2)