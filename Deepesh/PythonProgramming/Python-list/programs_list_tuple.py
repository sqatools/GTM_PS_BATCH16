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
print("result :", result)