add = lambda x, y : x + y

sub = lambda x, y : x - y

multi = lambda x, y : x*y

div = lambda x, y : x/y

if __name__ == "__main__":
    print("Enter two numbers")

    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))

    while(True):
        print("Enter your choice...")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            print(add(a,b))
        
        elif choice == 2:
            print(sub(a,b))

        elif choice == 3:
            print(multi(a,b))

        elif choice == 4:
            print(div(a,b))

        else:
            print("wrong input given")
