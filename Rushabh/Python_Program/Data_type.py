####################################
print("#"*50)
# sort() method: this method sort list data in ascending descending order, 
# and modify the original list.
list_h = [5, 7, 8, 9, 2, 3, 1]
list_h.sort()
print("Ascending order :", list_h) # [1, 2, 3, 5, 7, 8, 9]

list_j = [5, 7, 8, 9, 2, 3, 1]
list_j.sort(reverse=True)     
print("Descending order :", list_j) # [9, 8, 7, 5, 3, 2, 1]

#############
# sorted function :  it returns the sorted value in ascending
# in descending order without modifying original list
list_k = [5, 7, 8, 10, 20, 9, 2, 3, 1]
result =  sorted(list_k)
result2 = sorted(list_k, reverse=True)
print("ascending result :", result) # [1, 2, 3, 5, 7, 8, 9, 10, 20]
print("descending result :", result2)  # [20, 10, 9, 8, 7, 5, 3, 2, 1]


list_l = [5, 7, 8, 10, 20, 9, 2, 3,10,20, 1]
result=sorted(list_l)
print("sorted list :", result) # [1, 2, 3, 5, 7, 8, 9, 10, 10, 20, 20]  
result2 = sorted(list_l, reverse=True)
print("sorted list in descending order :", result2) # [20, 20, 10, 10, 9, 8, 7, 5, 3, 2, 1]
