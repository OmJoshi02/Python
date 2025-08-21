a = int(input("enter the 1st number :"))
b = int(input("enter the 2nd number :"))
c = int(input("enter the 3rd number :"))
if a > b and a>c:
    print(f"1st number which is {a} the max of three number. ")
elif b>a and b>c:
    print(f"2nd number which is {b} the max of three numbers. ")
else:
    print(f"3rd number which is {c} the max of three numbers. ")
