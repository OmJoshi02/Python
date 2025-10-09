from yaml import safe_load_all


class Employee:
    def __init__(self, name, age, salary): #Parameterized constructor
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print("Name of Employee : ", self.name)
        print("Age of Employee : ", self.age)
        print("Salary of Employee : ",self.salary)


obj1 = Employee("Om", 20, 1000000)
obj1.display()
print()
obj2 = Employee("Gandhar", 20, 2000000)
obj2.display()

