set = {1,2,3,4,4,5}
print(set)

#Functions of set
set.add(8) #It can add only one argument at one time
print(set)

set.update([11,12,13]) #It can add multiple elements at one time
print(set)

set.remove(12)
print(set)
set.discard(5)
print(set)

print(set.pop()) #Pops random element 



a = {1,2,3}
b = {2,3,4}
print(a.intersection(b)) #Returns common element

print(a.union(b)) #combines two different sets

print(a.issubset(b)) #Returns True if all items of this set is present in another set

print(a.issuperset(b)) #Returns True if all items of another set is present in this set

print(set.clear()) #Clears all the set