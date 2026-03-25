## write a python program to remove duplicate characters from given string 

str1 = "python programming language"
output =""

for char in str1: 
    if char not in output :
        output = output + char
    else:
        continue

print(output)


## Program to remove all the duplicte words 

print("-"*50)

str2 = " Ravi Rahul Pavan Rohan Rohit Rahul Ronak Rohan"
out2= str2.split()
print(out2)

out1= []
for i in out2 :
    if i not in out1:
        out1.append(i)
    else:
        continue
    
print(out1)


##program to get a string made of first & last 2 chars from a given string. 
# If the string length is less than 2, return instead of the empty string

str1 = "python"

if len(str1) < 2 : 
    print("given string length is less than 2")
else :
    print(str1[0] + str1[-1])


##string program that takes a list of strings & returns the length of the longest string.

str_list = ["python", "programming","is", "Easy", "to", "learn"]  

max = 0
for i in str_list:
    if len(i) > max:
        max = len(i)
        long_str = i
print("The length of the longest string is: ", max, long_str)


print("-"*50)

##to get a string made of 4 copies of the last two characters of a specified string 
# (length must be at least 2).
str1 = "om "
if len(str1) < 2:
    print("given string length is less than 2")
else:
    print(str1[-2:]*4)

print("*"*50)

#Python string program to reverse a string if it’s length is a multiple of 4.

str1 = "programs"
if len(str1)%4 == 0 :
    print(str1[-1::-1])


print("$"*50)

## Python string program to count occurrences of a substring in a string.




str1 = "Practising Python Programs"
str2 = "Pr"
count = 0

if str2 in str1: 
    count = count + 1
    print("occurred in the given string is : ",count)
