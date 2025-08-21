n = int(input("enter the number to check :"))

original = n 
rev_num = 0

while n > 0:
    digit = n%10
    rev_num = rev_num * 10 + digit 
    n = n // 10

if original == rev_num :
    print(f"the number U entered {n} is the palindrome...")
else :
    print(f"entered number {n} is not the palindrome")