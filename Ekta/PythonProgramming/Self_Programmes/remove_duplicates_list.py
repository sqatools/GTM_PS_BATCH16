list=[10,60,20,50,40,80,100,20,60,75,85]

print("After removing duplicates from list using set",set(list))
count=len(set(list))
print("Count of elements from list--->",count)
print("*"*50)
print("Remove duplicates using for loop concept")
duplilist=[]
for element in list:
    if element not in duplilist:
        duplilist.append(element)

print("The list with removed duplicates using for loop",duplilist)
print("Count after removing duplicates ",len(duplilist))
