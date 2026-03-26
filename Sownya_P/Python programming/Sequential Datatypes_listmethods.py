## list declaration

l1 = [ 1, 234.33 , "avfde", [1,2,3], (5,7,9),{'a':123}, {5, 6, 7}, True]

print(type(l1))
print(l1)
print(l1[2])  ## positive indexing
print(l1[3][1])
print("*"*50)

print(l1[-2])  ## negative indexing

## slicing a list
print("printing with specific range = ", l1[0:3:1])
print("elements in a list without range =",l1[:])  # will print as is

print("printing in range of negative = " ,l1[::-1])  ## reverse the list

print("-"*50)

## list methods
## adding one element to list
print("before appending : " ,l1)
l1.append(500)
l1.append("python")
print("after appending ",l1)

print("-"*50)

## adding an element in particular position

l1.insert(2,12348765432)
print(l1)


## extend method is used to add 1 list to another , original list will be modified after adding

list1 = [2,4,5]
list2 = ['a','b','c']

print("adding a list to other list ",list2.extend(list1)) ## as it doesnt return any value

print(list2)

## list concatination

print("adding 2 lists : ", list1+list2)

list3= list1+list2
print(list3)

## remove any speccific value from the list
list_d = [6 ,8,10,15,234,"qwerty"]
print(list_d)
list_d.remove(15)
print(list_d)
print(type(list_d))

## pop method to remove from specific position

print(list_d)
print("poping the element : ",list_d.pop())
print(list_d)
list_d.pop(1)
print(list_d)

## clear method to remove complete data from a list

list_d.clear()
print("clearing the elements : ",list_d)

## reverse method will reverse the elements in a list and modify the list

list_e = [ 12, 234.33 , 19,45678 , 5, 34]
print(list_e)
list_e.reverse()
print(list_e)
## reversed can be stored in a variable where as reverse wont return any value
result = list(reversed(list_e))
print(result)

## sort method for arranging the elements in ascending and descending orders and doesnt modify the original list

list_e.sort()
print(list_e.sort())  ## return none

print("ascending order ", list_e)

list_e.sort(reverse=True)
print("descending order", list_e)

## sorted method will not be modifying the original list
print(sorted(list_e))

print(sorted(list_e, reverse=True))

## ## max , min and sum methods

List_f = [ 12, 234.33 , 19,45678 , 5, 34]
print("max value in list : ", max(List_f))
print("min value in list : ", min(List_f))
print("sum of all the elements in list : ", sum(List_f))