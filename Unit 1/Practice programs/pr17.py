n = int(input("How many numbers? "))
i = 1
largest = 0 

while i <= n:
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num
    i += 1

print("The largest number is:", largest)
