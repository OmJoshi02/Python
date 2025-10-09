from abc import ABC, abstractmethod  # Abstract method


class Boss(ABC):

    def task1(self):
        print("task1 completed")

    def paysal(self):
        print("60k")


class Emp(Boss):
    def taks1(self):
        print("Task1 completed")


class Emp2(Boss):
    def task1(self):
        print("Task 2 completed")

e = Emp()
e.task1()
e.paysal()

e2 = Emp2()
e2.task1()
e2.paysal()
