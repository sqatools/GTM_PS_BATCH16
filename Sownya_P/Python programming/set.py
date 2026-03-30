set1= {10 ,23.4,"python", (1,2,3), True, 10}  ## set will not allow duplicate values    
print(type(set1))
print(set1)


print("*"*50)

## set Methods 

## set union method to combine 2 sets

set1 ={ 10, 3.4, 55, "a",'b','c'}
set2 = { 20, 3.4, 55, "b",'e','f'}

print("union of 2 sets : ", set1.union(set2))

## intersection of 2 sets - common elements in both sets
print("intersection of 2 sets : ", set1.intersection(set2))

## difference of 2 sets - elements in set1 which are not in set2
print("difference of 2 sets : ", set1.difference(set2))

## symmetric difference of 2 sets- elements which are in set1 or set2 but not in both
print("symmetric difference of 2 sets : ", set1.symmetric_difference(set2))

print("*"*50)

## adding an element to set using add() method
set1.add(100)
print(set1)


#remove some element from set using remove() method

set1.remove(3.4)
print(set1)

## remove an element from a set randnomly using pop() method
print("before pop : ", set1)
set1.pop()
print("after pop : ", set1)

## discard method to remove an element from set if it is present in the set otherwise it will not throw any error
set1.discard(55)    
print(set1)
set1.discard(500)  ## as 500 is not present in the set it will not throw any error
print(set1) 