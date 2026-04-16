#1). Python Dictionary program to add elements to the dictionary.
dict1 = {"name":"Thangam", "age": 43,"email": "t.thangam@gmail.com"}
print(dict1)
"""Python Dictionary program to print the square of all values in a dictionary.
Input : {‘a’: 5, ‘b’:3, ‘c’: 6, ‘d’ : 8}
Output :
a : 25
b : 9
c : 36
d : 64"""
iPut = {'a': 5, 'b':3, 'c': 6, 'd' : 8}
oPut = {}
for i,j in iPut.items():
    oPut[i] = j*j
print(oPut)
"""Python Dictionary program to move items from dict1 to dict2.
Input :
dict1 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
dict2 = {}
Output :
dict1 = {}
dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}"""
dict1.update(dict2)



