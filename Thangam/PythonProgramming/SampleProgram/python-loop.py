"""1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
Input1:1500
Input2:2700"""
for i in range(1500, 2701, 1):
    if i%7==0 and i%5==0:
        print("numbers which are divisible by 7 and multiple of 5",i)
"""Python Loops program that will add the word from the user to the empty string using python.
Input: “python”
Output : “python”"""
word = input("Enter the word python:")
str1 = ""
for i in word:
    str1 += i
print("Word:",str1)
"""Python Loops program to count the number of even and odd numbers from a series of numbers using python.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers: 4
Number of odd numbers: 5"""
for i in range(1, 10, 1):
    evenNum = 0
    oddNum = 0
    if i%2==0:
        evenNum += 1
    else:
        oddNum += 1
    print("even numbers count:",evenNum)
    print("odd numbers count:", oddNum)

# write a program to get all people age which are eligible to vote
list1 = [6, 7, 9, 23, 45, 12, 68, 24, 18]
for age in list1:
    if age >= 18:
        print("Eligiable to vote:", age)

//print("domain :", url.split("//")[1].split(".")[0])  # facebook
url = "https://facebook.com"
l1 = url.split("//")
s1 = l1[1]
l2 = s1.split(".")
s2 = l2[0]


