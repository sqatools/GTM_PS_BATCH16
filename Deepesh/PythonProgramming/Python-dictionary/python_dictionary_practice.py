dict1 = {'a' : 123, 'b': 456, 'c': 63}
print("dict1", dict1, type(dict1))

# get value from dictionay
print(dict1['a']) # 123

# add new key to the dictionary
dict1['d'] = 897
print(dict1)
# {'a': 123, 'b': 456, 'c': 63, 'd': 897}

dict2 = {"students" : [
                        {'name': 'rahul', 'age':25, 'email': 'rahul@gmail.com'},
                        {'name': 'rohit', 'age':30, 'email': 'rohit@gmail.com'}
                     ],
         "teachers": [
                        {'name': 'Mrs Pooja', 'age':45, 'email': 'pooja@gmail.com'},
                        {'name': 'Mrs Verma', 'age':50, 'email': 'mrsverma@gmail.com'}
             
                 ]}
print(dict2['students'][0]['email']) # rahul@gmail.com
print(dict2['teachers'][1]['email']) # mrsverma@gmail.com


################## dictionary methods ###########################
print(dir(dict))

"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
 'pop', 'popitem', 'setdefault', 'update', 'values'
"""

# 1. get method: get any specific value with key
dict3 = {'a': 123, 'b': 456, 'c': 63, 'd': 897}
print(dict3.get('d')) # 897

# 2. keys and values method.
print("keys list :", dict3.keys()) # dict_keys(['a', 'b', 'c', 'd'])
print("key value :", dict3.values()) # dict_values([123, 456, 63, 897])

# 3. items() :  this method will return key value pair in tuple.
print("key value pair :", dict3.items())
# dict_items([('a', 123), ('b', 456), ('c', 63), ('d', 897)])

# 4. Update method: This method update one dictionart data to another dictionary
dict_a = {'P': 88, "Q": 99, "R": 123, "M": 709}
dict_b = {'M': 102, "N": 456, "O": 123}
dict_b.update(dict_a)
print("dict_b :", dict_b)
# {'M': 102, 'N': 456, 'O': 123, 'P': 88, 'Q': 99, 'R': 123}
print("dict_a :", dict_a)
# {'P': 88, 'Q': 99, 'R': 123}

print("_"*50)
#copy method:

# shallow copy
dict_x = {'P': 88, "Q": 99, "R": 123, "M": 709}
dict_y = dict_x
dict_y['S'] = 500
dict_x["T"] = 78

print("dict_y :", dict_y) # {'P': 88, 'Q': 99, 'R': 123, 'M': 709, 'S': 500, 'T': 78}
print("dict_x :", dict_x) # {'P': 88, 'Q': 99, 'R': 123, 'M': 709, 'S': 500, 'T': 78}

# Deep Copy : student try it.
dict_b = {'M': 102, "N": 456, "O": 123}


##################################################

dict_11 = {'P': 88, 'Q': 99, 'R': 123, 'M': 709, 'S': 500, 'T': 78}
for k, v in dict_11.items():
    print("key:", k, "value :", v)

"""
key: P value : 88
key: Q value : 99
key: R value : 123
key: M value : 709
key: S value : 500
key: T value : 78
"""

print("_"*50)
###################################################
# create a dictinary with given string when word as key and length of word as value
str1 = "We Are Learning Python Programming"
result = {}
word_list = str1.split()
for word in word_list:
    result[word] = len(word)


print("Result :", result)
# {'We': 2, 'Are': 3, 'Learning': 8, 'Python': 6, 'Programming': 11}

# Pop 

dict12 = {'We': 2, 'Are': 3, 'Learning': 8, 'Python': 6, 'Programming': 11}
val = dict12.pop('We')
print("return value :", val) # return value : 2
print("dict12:", dict12) # {'Are': 3, 'Learning': 8, 'Python': 6, 'Programming': 11}