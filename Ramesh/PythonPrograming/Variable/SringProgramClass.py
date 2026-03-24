# 


str1 = "Learning Python is Fun"

output = ""

for char in str1:
    if char not in output:
        output = output + char
    else:
        continue

print(output)


#2 write a python program to remove duplicate words.

str2 = "Rahul Ravi Rohan Rohit Rahul Ravi Ronak Rohan"

output = ""
for word in str2.split(" "):
    print(output)
    if word not in output:
        output = output + word + ""
    else:
        continue
print(output)


#3 write a program to longest word from given string .

str3 = "India won third t20 cricket world cup"
longest = ""

for word in str3.split(" "):
    print (longest)
    if len(word) > len (longest):
        longest = word
    else:
        continue
print(longest)


#4 Write a Python program to get a string made of the first and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string

str4 = "pr"
result = str4[:2] + str4[-2:]

if len(str4) < 2:
    print("")
else:
    result 
print(result)


#5  Python string program that takes a list of strings and returns the length of the longest string.

str5 = ["India", "is", "best", "cricket", "team"]
longest = ""

for word in str5:
    if len(word) > len(longest):
        longest = word
    else:
        continue
print(longest)

#6 Python string program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)

str6 = "Python"
print(str6[-2:]*4)


#7 Python string program to reverse a string if it’s length is a multiple of 4.

str7 = "Python"

if len(str7) % 4 == 0:
    print(str7[0 : 5 :-1])
else:
    print(str7)


#8  Python string program to count occurrences of a substring in a string.


str8 = "Python is easy to lewarn and it is a programming language"

print(str8.count("a"))


# 9 Python string program to test whether a passed letter is a vowel or consonant.

str9 = "a"
