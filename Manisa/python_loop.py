#20_03_2026

for i in range(1, 5):
    print("value of i:", i)
    print("---------------------")
    for j in range(1, 4):
        print("value of j:", j)

    print("-------------------------")

#program to check prime number
num = 15
prime = True
for i in range(2, num):
    if num % i == 0:
        prime = False
        break

if prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

#multiple loop for checking prime number from 2 to 100

for num in range (2, 101):
    prime = True
    for i in range(2, num):
        #print(i)
        if num % i == 0:
            prime = False
            break

    if prime:
       print(num, "is a prime number")
    #else:
        #print(num, "is not a prime number")


#while loop - condition based loop

n = 1
while n <= 5:
    print("value of n:", n)
    n += 1 #n = n + 1

 #infinite loop using while loop
n = 1
while (True):
    print("value of n:", n)
    n += 1 #n = n + 1
    #infinite loop will run until we stop it manually, so we can use break statement to stop the loop when a certain condition is met
    if n == 101:
        break

#loop programs
#divisible by 5 and 7

for n in range(1500, 2700):
    if n%5 == 0 and n%7 == 0:
       print(n, ": number is divisible by 5 and 7")

#Python Loops program that will add the word from the user to the 

input = "python"
output= ""
for i in range(len(input)):
    print("value of i:", i)
    #output = input[i] + output
    output = output + input[i]
print(output)

#write program to check odd and even number
input = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for n in input:
    if n%2 == 0:
        print(n, ": number is even")
    else:
        print("number is odd", n)

#write program print all numbers from 0 to 6 except 3 and 6

for n in range(0, 7):
    if n == 3 or n == 6:
        continue
    print(n)

"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
        print(j, end=" ") #print the value of j after the star
    print() #print a new line after each row of stars
    