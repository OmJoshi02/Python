class Employee:
    """This is Employee class"""

    company = "Microsoft"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


print("Class name : ",Employee.__name__)
print("Module name : ", Employee.__module__)
print("Base classes : ", Employee.__bases__)
print("Class Dictionary ", Employee.__dict__)
print("Documentation String", Employee.__doc__)
