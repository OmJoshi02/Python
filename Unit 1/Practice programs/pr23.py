num = int(input("enter the number"))

result = 1.0 
fact = 1

for i in range(1,num+1):
    fact *=i
    result += 1/fact    

print (result) 