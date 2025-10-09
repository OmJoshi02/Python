class demo:

    var1 = "Hii"

    def __init__(self, var1="Hello"): #Default constructor
        self.str = "World"
        self.var1 = var1

    def __del__(self):
        print("Destructor called")


    def display(self):
        print(self.var1)
        print(self.str)

obj = demo()
obj.display()
del obj