str3 = "Python is a great programming language"

list3 = str3.split(" ")  # splits the string into a list of words
print(list3)
print(len(''))
longest_word = ""
smallest_word = ""
small_word_len= float("inf")
for a in list3:
    if len(a) > len(longest_word):
        longest_word = a
    
    if len(a) < small_word_len:
        small_word_len = len(a)
        smallest_word = a

print("smallest word=",smallest_word)
print("longest word=",longest_word)

print("------------------------")

#########################################

for i in range(1, 6): #row
    #print("i-", i)
    for j in range(1, i+1): #column
        print("*", end = " ")
        #print("j-", j)
    print()
print("----------------------------")
for i in range (5, 1, -1):
    for j in range(i, 1, -1):
        print("*", end=" ")
    print()