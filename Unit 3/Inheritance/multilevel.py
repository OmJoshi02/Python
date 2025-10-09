class GrandParent:
    def display_grandparent(self):
        print("This is the GrandParent class")

class Parent(GrandParent):
    def display_parent(self):
        print("This is the Parent class")

class Child(Parent):
    def display_child(self):
        print("This is the Child class")

obj = Child()
obj.display_grandparent()
obj.display_parent()
obj.display_child()
