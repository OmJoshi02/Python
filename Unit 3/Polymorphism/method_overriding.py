#Method overriding

class Parent:

    def car(self):
        print("Suzuki")

class Child(Parent):
    def car(self):
        print("BMW")

c = Child()
c.car()