#Arithmetic operators
a = 20
b = 10

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#Comparison operators

print("a > b : ",a > b)
print("a < b : ",a<b)
print("a >= b :",a >= b)
print("a <= b : ",a <= b)
print("a == b : ",a == b)
print("a != b : ",a != b)

#Logical operators
if a == 10 and b == 20:
    print("True")
else:
    print("False")

if a or b == 20:
    print("True")

else:
    print("False")

#Identity Operators : is, is not
print(a is b)
print(a is not b)

x = "Hello"
#Membership operators : in, not in
print("o" in x) #true
print("o" not in x) #false