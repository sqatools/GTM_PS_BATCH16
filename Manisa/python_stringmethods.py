str1 = "Hello"
str2 = "world"

# Concatenation
str3 = str1 + " " + str2
print(str3)  # Output: Hello world
print(str1+" "+str2)  # Output: Hello world

num = 23
str5 = str1+" " +str2+str(num)
print(str5)  # Output: Hello world23

#f string format

name = "Alice"
age = 30
city = "New York"
# Using f-string for formatting

formatted_string = f"My name is {name}, I am {age} years old, and I live in {city}."

print(formatted_string)  # Output: My name is Alice, I am 30 years old, and I live in New York.

#string slicing
# str [start:stop:step]

str6 = "Python Programming"
print(str6[0:6])  # Output: Python
print(str6[7:18])  # Output: Programming
print(str6[1:8:2])  # Output: yhnP
print(str6[7::])  # Output: Programming
print(str6[:6])  # Output: Python

#default start value is zero and default stop value is the length of the string
#default step value is 1

print(len(str6))  # Output: 18

print(str6[::-1])  # Output: gnimmargorP nohtyP (reverses the string)

#string methods
#upper(), lower(), title(), strip(), replace(), split(), join()

str7 = "   Hello World   "
print(str7.upper())  # Output:    HELLO WORLD   
print(str7.lower())  # Output:    hello world
print(str7.title())  # Output:    Hello World
print(str7.strip())  # Output: Hello World
print(str7.replace(" ", ""))  # Output: HelloWorld
print(str7.replace("world", "Manisa"))  # Output:    Hello Manisa
print(str7.split())  # Output: ['Hello', 'World']

str8 = ["Hello", "World"]
print(" ".join(str8))  # Output: Hello World

str_m = "PYTHON"
print("*".join(str_m))  # Output: P*Y*T*H*O*N (joins the characters of the string with a specified separator)


print(str7.swapcase())  # Output:    hELLO wORLD    (swaps the case of each character)

str_a = "python is easy to learn"

#count method counts the number of occurrences of a substring in a string
print(str_a.count("o"))  # Output: 2
print(str_a.count("python"))  # Output: 1

#index method returns the index of the first occurrence of a substring in a string
print(str_a.index("easy"))  # Output: 10
print(str_a.index("to"))  # Output: 15
print(str_a.index("i"))  # Output: 7

#split method splits a string into a list of substrings based on a specified delimiter (default is whitespace)
str_b = "India-best-cricket-team"

str_c = "automation,with,AI"

print(str_b.split("-"))  # Output: ['India', 'best', 'cricket', 'team']
print(str_c.split(","))  # Output: ['automation', 'with', 'AI']

url = "https://www.insta.com"
print("domain :", url.split("//")[1].split(".")[1])  # Output: domain : insta

str_b = "India best cricket team, best players"
print(str_b.replace("best", "great"))  # Output: India great cricket team, great players
print(str_b.replace("best", "great", 1))  # Output: India great cricket team, best players (replaces only the first occurrence)