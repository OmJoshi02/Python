class Parent:
    def display_parent(self):
        print("This is the Parent class")

class Child(Parent):
    def display_child(self):
        print("This is the Child class")

# Object of Child
obj = Child()
obj.display_parent()  # from Parent
obj.display_child()   # from Child
