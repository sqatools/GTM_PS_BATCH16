dict1 = {'a' : 123, 'b' : 456, 'c' : 789}
print(dict1, type(dict1))

# get value from dectionary
print(dict1['a'])

#add ne key to the dictionary 
dict1['d'] = 897
print(dict1)


dict2 = {"students" : [
                        {'name' : 'rahul', 'age' : 25, 'email' : 'rahul@gmail.com'},
                        {'name' : 'rohit', 'age' : 30, 'email' : 'rohit@gmail.com'}
                    ],
         "teachers": [
                        {'name' : 'Mrs Pooja', 'age' : 45, 'email' : 'pooja@gmail.com'},
                        {'name' : 'Mrs Verma', 'age' : 50, 'email' : 'mrsverma@gmail.com'}
             
                    ]}

print(dict2['students'][0]['email'])
print(dict2['teachers'][1]['email'])



################################# dictionary methods ##################################

#1. get method : get any specific value with key

dict3 = {'a': 123, 'b': 456, 'c': 789, 'd': 897}
print(dict3.get('d'))

# 2. key and values method.

print("key list :", dict3.keys())
print("key value :", dict3.values())


# 3. items() : this method will return key value pair in pair in tuple.
print("key value pair :", dict3.items())

# 4. update method : 

dict_a = {'P' : 88, "Q" : 99, "R" : 123}
dict_b = {'M' : 102, "N" : 102, "O" : 123}
dict_b.update(dict_a)
print(dict_a)
print(dict_b)

# copy method :

dict_x = {'P' : 88, "Q" : 99, "R" : 123, "M" : 709}
dict_y = dict_x
dict_y['S'] = 500
dict_x["T"] = 78

print(dict_x)
print(dict_y)


# Deep copy : student try it.

dict_b = {'M' : 102, "N" : 102, "O" : 123}




##############################################################

dict_11 = {'P': 88, 'Q': 99, 'R': 123, 'M': 709, 'S': 500, 'T': 78}
for k, v in dict_11.items():
    print(k, v)



#########################################################
# create a dictionary with given string when word as key and length of word as value 

str1 = "We Are Learning Python"
result = {}

word_list = str1.split()
for word in word_list:
    result[word] = len(word)

print(result)