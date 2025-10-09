class Parent:
    def display_parent(self):
        print("This is the Parent class")

class Child1(Parent):
    def display_child1(self):
        print("This is Child1 class")

class Child2(Parent):
    def display_child2(self):
        print("This is Child2 class")

# Create objects
obj1 = Child1()
obj2 = Child2()

obj1.display_parent()
obj1.display_child1()

obj2.display_parent()
obj2.display_child2()
