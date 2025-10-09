class GrandParent:
    def show_grandparent(self):
        print("This is GrandParent class")

class Father(GrandParent):
    def show_father(self):
        print("This is Father class")

class Mother:
    def show_mother(self):
        print("This is Mother class")

class Child(Father, Mother):
    def show_child(self):
        print("This is Child class")

obj = Child()
obj.show_grandparent()
obj.show_father()
obj.show_mother()
obj.show_child()
