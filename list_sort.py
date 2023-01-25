gro= ["biskit","it2" , "it3","it4", 560]
number = [12,13,14,20,15,18,16]
print(number[-1:-8:-2])
los = [[1,3],[5,4]]
a = input("enter the number")
print(gro)
print(number)
number.sort()#this will change original list
print(number)
number.reverse()
print(number)
number.append(a)
print(number)
number.insert(2, 100)#it is used to insert numbers at specific position
print(number)
number.pop()#it is used to remove last element
print(number)
number.remove(20)
print(number)
number[4]= 99 # lists can be manuplated
print(number)
# so we use tuples
tup=(6,2,5)# this cant be manupulated
number[6] =50000000
print(number)
print(los[0][0])
number.extend(number)
print(number)
# # sort function dos't return any value and change the original list but sorted function return sorted list and not change original value 
