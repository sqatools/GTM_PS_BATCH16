str1= "Learning Python is very easy and interesting"
output = ""

for i in str1:
    if i not in output:
        output = output + i 
    else:
        continue

#WAP python program to remove duplicate words from the string and print the unique words in the string.

str2 = "Rahul Ravi Rohan Rohit Rahul Ravi Ronak Rohan Rohit"
output2 = ""    
  
for j in str2.split():
    if j not in output2:
        output2 = output2 + j + " "
    else:
        continue

print(output2)


# WAP python program to find the longest word from the string.
str3 = "India won the third t20 cricket world cup"
longest_word = ""

for word in str3.split():
    if len(word) > len(longest_word):
       longest_word = word
print("Longest word:", longest_word)

# Python string program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
str4 = "Python"

if len(str4) >= 2:
    last_two_chars = str4[-2:]
    result = last_two_chars * 4
    print(result)

    
# Reverse a string if its length is multiple of 4.
str5 = "Helloworld12"  
if len(str5) % 4 == 0:
    reversed_str = str5[::-1]
    print(reversed_str)

# Python string program to count occurrences of a substring in a string.
str6 = "Python is a great programming language. Python is widely used."
substring = "Python"    

count = str6.count(substring)
print(f"The substring '{substring}' occurs {count} times in the string.")   