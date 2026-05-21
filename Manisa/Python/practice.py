list2 = [5, 10, 7, 23, 12, 5, 7, 35, 45]
for n in list2:
    if n%5 == 0:
        print(n)
        print ("square value of number is:", n**2)

###########################

list1 = [6, 7, 9, 23, 45, 12, 68, 24, 18]
for age in list1:
    if  age >= 18:
        print(age)
        print("you are eligible")


#####write a program to remove duplicates from  below string######

str2 = "Rahul, Ravi, rohit, Rahul, Ravi, rohit, ronak, Rishabh"
list1 = str2.split(",")

list2 = []

for name in list1:
    if name not in list2:
        list2.append(name)

print(list2)
str2 = "Rahul, Ravi, rohit, Rahul, Ravi, rohit, ronak, Rishabh"
str3 = "Python is a great programming language"
list3 = str3.split(" ")  # splits the string into a list of words
print(list3)

print(len('')) #to get value of '' space

longest_word = ""
smallest_word = ""
length_of_smallest_word = 2

print(len(smallest_word))#to get value of "" nothing

longest_word = list3[0]
smallest_word = list3[0]

for a in list3:
    if len(a) > len(longest_word):
        longest_word = a
    
    if len(a) < len(smallest_word):
        smallest_word = a

print("smallest word=",smallest_word)
print("longest word=",longest_word)



#####python program to write longest word in a string######

str3 = "Python is a great programming language"

x=10
print("datatype:", type(x))
y = "x"
print("datatype:", type(y))
y = x
print("datatype:", type(y))

y = str(x)
print("datatype:", type(y))

#2). Python string program that takes a list of strings and returns the length of the longest string.

str3 = "Python is a great programming language        "

list_A = str3.split(" ")  # splits the string into a list of words
print(list_A)


longest_word = list_A[0]
smallest_word = list_A[0]

for a in list_A:
    if len(a) > len(longest_word):
        longest_word = a
    
    if len(a) < len(smallest_word):
        smallest_word = a

print("smallest word=",smallest_word)
print("length of smallest word", len(smallest_word))
print("longest word=",longest_word)
print("length of longest word", len(longest_word))

#1). Write a Python program to get a string made of the first and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string

str_A ="great to be hevyio"

a=str_A[:2:]
print(a)

len_str = len(str_A)

b=str_A[len_str - 2:len_str:]
print(b)

print(a + b)

string = "sqatools"

#Printing output
if len(string) < 1:
    print(True)
else:
    print(string[:2]+string[-2:])