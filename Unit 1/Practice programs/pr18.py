n = int(input("How many numbers? "))
i = 1
smallest = 999999  

while i <= n:
    num = int(input("Enter a number: "))
    if num < smallest:
        smallest = num
    i += 1

print("The smallest number is:", smallest)
