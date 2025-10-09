# Define custom exception
class AgeTooSmallError(Exception):
    def __init__(self, message="Age is too small! Must be 18 or older."):
        self.message = message
        super().__init__(self.message)

# Using the custom exception
age = int(input("Enter your age: "))

try:
    if age < 18:
        raise AgeTooSmallError  # Raise your custom exception
    else:
        print("Access granted!")
except AgeTooSmallError as e:
    print("Error:", e)
