#Build a simple command-line calculator that performs basic arithmetic: addition, subtraction, multiplication, and division.
import sys


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    if a > b and b != 0:
        return a/b
    else:
        return "Error divide by 0 exception"

if __name__ == "__main__":

    while(True):
        print("=============Menu============")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            a = int(input("Enter First Number : "))
            b = int(input("Enter Second Number : "))
            print(add(a,b))

        elif choice == 2:
            a = int(input("Enter First Number : "))
            b = int(input("Enter Second Number : "))
            print(sub(a,b))

        elif choice == 3:
            a = int(input("Enter First Number : "))
            b = int(input("Enter Second Number : "))
            print(multi(a,b))

        elif choice == 4:
            a = int(input("Enter First Number : "))
            b = int(input("Enter Second Number : "))
            print("Answer : ",div(a,b))

        elif choice == 5:
            sys.exit()

        else:
            print("Enter correct choice")




