##  1. Number is divisible by 3 or not  ###


num = 9
if num % 3 == 0:
    print("The number is divisible by 3")   
else:
    print("The number is not divisible by 3")

print("*"*50)


## 2. if else condition for printing the numbers that are divisible by 3


for i in range(1,30):
    if i % 3 == 0:
        print(i, "is divisible by 3",i)   
    else:
        print("The number is not divisible by 3",i)   


print("*"*50)

for i in range(1,30):
    if i % 3 == 0:
        print(i,end=" \n")  
    


print("-"*50)


##  If else program to assign grades as per total marks.  marks > 40: Fail , marks 40 – 50: grade C
#  marks 50 – 60: grade B , marks 60 – 70: grade A , marks 70 – 80: grade A+ , marks 80 – 90: grade A++
## marks 90 – 100: grade Excellent , marks > 100: Invalid marks

m =100
 #m = int(input("Enter the marks: "))
if m > 100:
    print("Invalid marks")
elif m > 90 and m <= 100:
    print("Grade: Excellent")
elif m > 80 and m <= 90:
    print("Grade: A++")
elif m > 70 and m <= 80:
    print("Grade: A+")
elif m > 60 and m <= 70:
    print("Grade: A")
elif m > 50 and m <= 60:
    print("Grade: B")
elif m > 40 and m <= 50:
    print("Grade: C")
else:
    print("Fail")



print ("-"*80)

##  check the given number divided by 3 and 5 

numb= 15
if numb % 3 == 0 and numb % 5 == 0:
    print("The number is divisible by both 3 and 5")    

##  program to print the square of the number if it is divided by 11

n1 = 22
if n1 % 11 == 0:
    print("The number is divisible by 11 and its square is: ", n1**2)

print("-"*50)

##  check given number is a prime number or not.

n2 = 121
if n2 > 1:      
    for i in range(2, int(n2/2)+1):
        if n2 % i == 0:
            print(n2, "is not a prime number")
            break           
    else:
         print(n2, "is a prime number")

