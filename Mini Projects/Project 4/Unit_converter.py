#Create a CLI app that converts units (like km to miles, Celsius to Fahrenheit) based on user input.
import sys


def miles(km):
    return km * 0.621371

def km(mile):
    return mile / 0.621371

def cel_to_fah(cel):
    return (cel * 9/5) + 32

def fah_to_cel(far):
    return (far - 32) * 5/9


if __name__ == "__main__":

    while True:
        print("====================Menu==================")
        print("1. Km to Miles")
        print("2. Miles to KM")
        print("3. Celsius to Fahrenheit")
        print("4. Fahrenheit to Celsius")
        print("5. Exit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            a = float(input("Enter Km : "))
            print(miles(a))

        elif choice == 2:
            b = float(input("Enter Miles : "))
            print(km(b))

        elif choice == 3:
            c = float(input("Enter Celsius : "))
            print(cel_to_fah(c))

        elif choice == 4:
            d = float(input("Enter Fahrenheit : "))
            print(fah_to_cel(d))

        elif choice == 5:
            print("Exiting...")
            sys.exit()

        else:
            print("Enter correct option")