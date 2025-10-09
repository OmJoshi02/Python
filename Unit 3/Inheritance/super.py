class Parent:
    def show(self):
        print("This is Parent method")

class Child(Parent):
    def show(self):
        super().show()  # call parent method
        print("This is Child method")

obj = Child()
obj.show()
