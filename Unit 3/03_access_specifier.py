
class Employee:
    def __init__(self, name, age, salary):
        self.name = name #Public
        self._age = age #Protected
        self.__salary = salary #Private

    def display(self):
        print("Public name : ", self.name)
        print("Protected age :", self._age)
        print("Private Salary : ", self.__salary)



obj = Employee("Om", 20, 10000000)
obj.display()
