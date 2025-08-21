fs = frozenset([1,2,3,4,5])

for i in fs:
    print(i)

#Indexing of set cannot be done because it is immutable

a = frozenset([1,2,3])
b = frozenset([4,5,6])

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.isdisjoint(b))
print(a.issubset(b))
print(a.issuperset(b))
print(len(fs))
print(sorted(fs))
