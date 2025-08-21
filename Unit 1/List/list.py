l1 = [1,2,3,"Hello",3.14]
print(l1)
print(type(l1))
print()
#Positive Indexing

print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])
print(l1[4])
print()

#Negative Indexing
print(l1[-5])
print(l1[-4])
print(l1[-3])
print(l1[-2])
print(l1[-1])
print()

#List positive slicing
list = [1,2,3,4,5]
print(list[:])
print(list[1:])
print(list[::])
print(list[:3])
print(list[0:3])
print()

#List negative slicing
print(list[-1])
print(list[-3:])
print(list[:-1])
print(list[-3:-1])
print()

#Loop in list

name_list = ["John", "David", "James", "Tony"]
for i in name_list:
    print(i, end =" ")


print()
#List functions

list1 = [30,10,20,50,40,60,90]
list1.append(100)
print(list1)

list1.sort()
print(list1)  # [10, 20, 30, 40, 50, 60, 90]

print(max(list1))  # 100

print(min(list1))  # 10

print(sum(list1))  # 400

print(list1.count(20))  # 1

list1.reverse()
print(list1)  # [90, 60, 50, 40, 30, 20, 10]

list1.append(100)
print(list1)  # [90, 60, 50, 40, 30, 20, 10, 100]

list1.insert(2, 25)  # Insert 25 at index 2
print(list1)  # e.g., [90, 60, 25, 50, ...]

list1.remove(50)
print(list1)

new_list = sorted(list1)
print(new_list)  # [10, 20, 25, 30, 40, 60, 90, 100]
