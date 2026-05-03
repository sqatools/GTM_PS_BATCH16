##
dict = {"a" : 1 , "b" : 2 , "c" : 3 , "d" : 4 }

print(dict)
print(type(dict))
print(dict["a"])

dict["e"]= 1234
print(dict)

dict2={
    "students" : { "sownya" :30 , "Govind" : 23 , "Siva" :3 , "Aditya" : 34} ,
    "details" : [ {"name":"sow","age":30,"mail":"sow@gmail.com"},
                  {"name":"Siva","age":23,"mail":"siva@gmail.com"} ]
}
print(dict2)



### dict methods :
## 1. get method

print(dict2.get("details"))

## 2. key and value method
print(dict2.keys())
print(dict2.values())

## 3.items -- will return key value pair in a tuple

print(dict2.items())

### Update method - updtaes one dictionary with other dictonary

dict_a = { "a" : 1 , "b" : 2 , "c" : 3 , "d" : 4 }
dict_b = {"p": 123 ,"q": 345,"c":765 }

dict_b.update(dict_a)
print(dict_a)
print(dict_b)

# shallow copy
dict_x = {'P': 88, "Q": 99, "R": 123, "M": 709}
dict_y = dict_x
dict_y['S'] = 500
dict_x["T"] = 78

print("dict_y :", dict_y) # {'P': 88, 'Q': 99, 'R': 123, 'M': 709, 'S': 500, 'T': 78}
print("dict_x :", dict_x) # {'P': 88, 'Q': 99, 'R': 123, 'M': 709, 'S': 500, 'T': 78}

# Deep Copy : try it.
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

# create a dict with a string as inout and we should print word as key and length as value

str1 = " we are learning python programming"
list1= str.split(str1)
print(str1)
print(list1)
result = {}
for x in list1 :
       result[x]= len(x)

print(result)


