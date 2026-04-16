# Integer data type
n1=0
n2=55
n3=15987912578963
print(n1, type(n1))
print(n2, type(n2))
print(n3, type(n3))
      
#Float Data Type

x1=0.0
x2=5.24
x3=78789.587596
print(x1, type(x1))
print(x2, type(x2))
print(x3, type(x3))    

# Sequence Data Type
#1.String
s1="Hellow ekta"
s2='Python'
s3='python programming'
s4="""We are learning Python. Its very interesting language."""
s5='''Pyhton is a high level programming language. It is widely used in data science, machine learning, web development and many more.'''

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

#+ve and -ve indexing in python

s4='python'
print("+ve indexing:", s4[3])
print("-ve indexing:", s4[-3])


# List 
l1=[10,20,30,40,50]
l2=[10,[5,10,85],'python',(3,5,6),True]

print(l1, type(l1))
print(l2, type(l2))
#print 10 from list l2
print(l2[1][1])

#tuple data type -- its same as list but its immutable
tuple1=(10,20,30)
tuple2=(100,3.57,'India',(4,7),{'a':578},{5,6,7},False)
print(tuple1)
print(tuple2)
print("Print value in dictionary " ,tuple2[4]['a'])

#Dictionary --It stores data in key and values . It contains only unique keys.

dict2={23:5.6,10.5:"Hello","Python":[6,7,8],(5,7,8):{'p':789,'Q':45,True:(1,2,3),'R':123}}
print("Data from dictionary", dict2)
#If duplicate keys are there then it will take the last value of that key
dict3={10:100,20:200,10:300}    
print("Data from dict3", dict3)
print(list(dict2.keys())[3][1])

#Set data type -- It is unordered collection of unique items. It is mutable but it does not allow duplicate values.
 #Mutable data types are not allowed with set ex: list,dictionary, set 
set1= {5,7,8,3.5,'Hello',(5,6,7),True}
print(set1)
print(set1, type(set1))

#Boolean 
b1=True
b2=False
print(b1, type(b1))
print(b2, type(b2))
a=100
b=200
print(a==b)


x = "Python"
print(x[-2])
