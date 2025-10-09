import os

def create_file():
    with open("sample.txt", "w") as file:
        file.write("This is a new file")
    print("File created")

def read_file():
    if os.path.exists("sample.txt"):
        with open("sample.txt", "r") as file:
            print("file contains : ", file.read())
    else:
        print("File doesnot exist")

def append_file():
    with open("sample.txt", "a") as file:
        file.write("This line is appended")
    print("data appended to file")

def delete_file():
    if os.path.exists("sample.txt"):
        os.remove("sample.txt")
        print("File deleted")
    else:
        print("File doesnot exist")

def seek_file():
    if os.path.exists("sample.txt"):
        with open("sample.txt", "r") as file:
            print("Reading first 10 characters : ")
            data = file.read(10)
            print("Data : ",data)

            file.seek(0)
            print("\nAfter seek(0) : ",file.read(0))

            file.seek(28)
            print("\n Seek to position 28 : ")

    else:
        print("File not exist")

options = {
    1: create_file,
    2: read_file,
    3: append_file,
    4: delete_file,
    5: seek_file
}

while(True):
    print("\n--- File Operations Menu ---")
    print("1. Create/Write File")
    print("2. Read File")
    print("3. Append File")
    print("4. Delete File")
    print("5. Seek File")
    print("6. Exit File")

    choice = int(input("Enter your choice : "))

    if choice == 6:
        print("Exiting...")
        break

    elif choice in options:
        options[choice]()

    else:
        print("Invalid choice...")