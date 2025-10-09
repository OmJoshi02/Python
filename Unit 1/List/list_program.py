l = []
n = int(input("Enter the number of elements you want to store : "))

for i in range(0, n):
    l.append(input("Enter the item name : "))
    
print("Printing list of items : ")

for j in l:
    print(j, end = " ")