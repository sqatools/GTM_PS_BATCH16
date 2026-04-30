
string="Ekta"
reverse= ""
for i in string :
    reverse = i + reverse
    print("Reverse is-->",reverse)
print("Reverse is-->",reverse)

text="HellowWorld"
reverse_text = text[::-2]
print("Reverse of text is-->",reverse_text)

my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
last_element = my_list[::-2]
print("Last element of the list is-->",last_element)


my_list = [1, 2, 3, 4, 5]

# Remove elements at indices 1 to 3
#my_list[1:4] = []
mylistnew=my_list[1:4]

# Print the updated list
print(mylistnew)