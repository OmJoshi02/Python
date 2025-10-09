# Method Overloading
# Function having same name but different parameters called method overloading in a class

class A:

    def add(self, a, b, c=0):
        if c == 0:
            return a + b

        else:
            return a + b + c


a1 = A()
print(a1.add(12, 1))
print(a1.add(12, 1, 5))