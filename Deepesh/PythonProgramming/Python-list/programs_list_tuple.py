# write python program remove all duplicate values from tuple.

tup1 = (4, 5, 6, 7, 4, 5, 2, 5, 6, 1)
list1 = []

for val in tup1:
    if val not in list1:
        list1.append(val)
    else:
        continue

print("list1 :", list1) # [4, 5, 6, 7, 2, 1]

result = []
[result.append(val) for val in tup1 if val not in result]
print("result :", result) # [4, 5, 6, 7, 2, 1]


list_a= [4, 6, 8, 12, 4, 52, 8, 9, 1]
for i in range(len(list_a)):
    for j in range(i+1, len(list_a)):
        if list_a[i]+list_a[j] == 10:
            print(list_a[i], list_a[j])