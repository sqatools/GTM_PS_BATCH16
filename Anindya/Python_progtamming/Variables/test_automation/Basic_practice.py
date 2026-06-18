# str1 = 'SQATools'

# print(str1*5)
# 

# a = 40
# b = 50
# c = 30

# print((a+b+c)/3)

# a = [45, 60, 61, 66, 70, 77, 80]

# s = sum(a)

# g = (s+1)/2
# print(g)

# num1 = 9

# print(num1**2)
# print(num1**3)

# a = 10
# b = 20

# a,b = b,a

# print(a)

# print(b)
#  (a2 + b2 = c2)
# a = 10
# b = 30

# print(a**2 + b**2)

# c = 10

# print(c**2)

# if (a**2 + b**2) == c**2:
#     print("Formula proved")

# else:
#     print("Np")

# for item in range(1,31):
#     if item % 3 ==0:
#         print("Item is divided by 3", item)
#         if item % 5 ==0:
#             print("Item is divided by 5 as well", item)
#         else:
#             pass


# s = [12,3,2,45,23,34,2]

# for item in s :
#     if item > 18:
#         print("Eligible for vote", item)


# s = [5,10,12,35,34,3,4,15]

# for item in  s :
#     if item %5 ==0:
#         print(item**2)


# for item in range(2,100):
#     prime = True
#     for j in range(2,item):
#         if item%j ==0:
#             prime = False
#             break
#     if prime:
#         print("The number is prime",item)

    # else:
    #     print('The number is not a prime number', item)


# i = 1

# while True:
#     print(i)
#     i = i +1
#     if i == 10:
#         break


# for item in range(1500,2701):
#     if item % 7 == 0 and item %5 ==0:
#         print(item)

# value = input("Enter the va;ue")

# s = ""

# for item in value:
#     s = s +item

# print(s)

# a =  (1, 2, 3, 4, 5, 6, 7, 8, 9)

# even = 0
# odd = 0

# for item in a :
#     if item %2==0:
#         even = even +1

#     else:
#         odd = odd +1

# print(even)
# print(odd)

# name = "Anindya"
# age = 30

# g = "the name is {1} and the age is {1}".format(name,age)


# print(g)


# a = 'Anindya iS a gOOd boy'

# # print(a.title())

# print(a.swapcase(

# url = "https://facebook.com"

# print(url.split("//")[1].split(".")[0])

# a = 'Anindya is a good boy Anindya is tough to understand Anindya is not bad'

# b = a.replace("Anindya","Partha")

# print(b)

# a = "Anindya"

# print(" ".join(a))

# Isnumeric

# Isalpha

# isalnum

# a = 'test12'
# b = 'test'
# c = '12'
# d = 'jdjd 123'
# print(a.isalnum())
# print(b.isalnum())
# print(c.isalnum())
# # print(d.isalnum())


# s = 'Leaning python  is fun'

# output = ""


# a = "Rahul Ravi Rahul Raj Rahul"

# g = a.split()

# f = []

# for item in g :
#     if item not in f :
#         f.append(item)
#     else:
#         pass

# print(" ".join(f))

# a = 'India won third cricket world cup'

# f = a.split()

# g = ""

# for item in f :
#     if len(item) > len(g):
#         g = item
#     else:
#         continue

# # print(g)

# a = input("Enter the value")

# if len(a)>=2:
#     s = a[:2]
#     s1 = a[-2:]
#     f =  s + s1
#     print(f)
    
# else:
#     print(a)


# a = ['we','are','new','today','we','are','learning','python']

# print(a[-1:-5:-1])

# a = [1,2,3]
# b = [4,5,6]

# b.extend(a)

# print(b)

# a = [1,2,3,4,5,6,7,8,90]

# d = list(reversed(a))

# print(d)

# a = [12,43,4,4.45,5,5,56,6,6,56]

# a.sort()

# print(a)

# a = [12,43,4,4.45,5,5,56,6,6,56]

# a.sort(reverse=True)

# print(a)

    # a = [12,43,4,4.45,5,5,56,6,6,56]

    # d = sorted(a)

    # print(d)

    # a = [12,43,4,4.45,5,5,56,6,6,56]

    # f = sorted(a,reverse=True)

#     # print(f)
# # a = [12,43,4,4.45,5,5,56,6,6,56]

# a = [1,2,30]
# b = [23,45]

# c = a +b

# print(c)


# a = [12,43,4,4.45,5,5,56,6,6,56]

# f = sorted(a)

# print(f)

# g = sorted(a,reverse = True)

# print(g)


# a = [12,3,4]

# b = a.copy()

# b.append(100)

# a.append(300)

# print(a)
# print(b)

# a = (10,23,40,12,10,34,23,40)

# l = [item for item in a if item not in l]

# print(l)

# a = "We are lesning Python"

# g = a.split()


# d = {}
# for item in g :
#     d[item] = len(item)

# print(d)


# l1 = [12,3,4,5,5]

# l1.pop()

# print(l1)

# s = {1,2,3,[2,32,3]}

# print(s)

# s = {1,2,3}
# b = {4,5,3}

# s.discard(3)

# print(s)


# a =12

# def func():
#     b = 23
#     def abc():
#         c = 78
#         print("Global", a)
#         # print("Non local", b)
#         print("Local", c)
#         nonlocal b
#         print("Non local",b)
#         b=2333
#         print("new non local", b)
#     abc()

# func()


# a = 12

# def func():
#     b = 34
#     def abc():
#         global a 
#         nonlocal b
#         c = 346
#         print("Global",a)
#         print("Non local",b)
#         print("Local",c)
#         a = 455
#         b = 89
#         print('After change the global', a)
#         print("After change the nonocal", b)
#     abc()
# func()


# import openpyxl

# def func(file_path,sheet_name):
#     wb = openpyxl.load_workbook(file_path)
#     sheet= wb[sheet_name]
#     max_row = sheet.max_row
#     max_col = sheet.max_column
#     for r in range(1,max_row+1):
#         for c in range(1,max_col+1):
#             print(sheet.cell(r,c).value, end=" ")
#         print()    
# path = "D://Test_1234.xlsx"
# func(file_path=path,sheet_name="Sheet1")

# import openpyxl
# path = "D://Test_1234.xlsx"
# def func(file_path,sheet_name,cell_name,cell_valu):
    
#     wb = openpyxl.load_workbook(file_path)
#     sheet = wb[sheet_name]
#     cell = sheet[cell_name]
#     cell.value = cell_valu
#     wb.save(path)

# func(path,"Sheet2","A1","Anindya6")    

# def func(file_path,content):
#     with open(file_path,"a") as f :
#         f.write(content)

# file = "Anindya233.txt"
# con = 'Text'

# func(file,con)

import json 

def func(filepath):
    with open(filepath,'r') as f :
        data = f.read()
        s = json.loads(data)
        return s

g = func(r"C:\Users\hp\Desktop\gitcode\GTM_PS_BATCH16\Anindya\Python_progtamming\Variables\test_automation\amla.json") 
print(g)

print(type(g))

print(g['Anindua'])

g['arnab'] = 34

g['Raju'] = 56

def func(path,new_contntn):
    with open(path,'w') as f :
        new_data = json.dumps(new_contntn)
        f.write(new_data)

func(r'C:\Users\hp\Desktop\gitcode\GTM_PS_BATCH16\Anindya\Python_progtamming\Variables\test_automation\amla.json',g)