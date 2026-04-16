# Write a program to remove duplicate words
Str1 = "Rahul Ravi Rohan Rohit Rahul Ravi Ronak Rohan"
lWords = Str1.split(" ")
oWords = ""
for word  in lWords:
    if word  not in oWords:
        oWords = oWords +" " + word
print(oWords.strip())

# Write a program  to longest words given string
Str2 = "Rahul Ravi Rohan Rohit Rahul Ravi Ronak Rohan Thangam"
lWords = Str2.split(" ")
print(lWords)
len1 = 0
myDic = {}
for word  in lWords:
    if len1 < len(word):
        len1 = len(word)
        myDic[len1] = word
print(len1)
print(myDic[len1])
#1). Write a Python program to get a string made of the first and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string
str5 = input("Enter the string:")
if len(str5) < 2:
    print(str5)
else:
    w1 = str5[:2]
    w2 = str5[-2:]
    print(w2)
print(w1+w2)
#Python string program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).



