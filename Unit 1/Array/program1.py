import array as arr

# Create array
numbers = arr.array('i', [10, 20, 30, 40])
print("Original:", numbers)

# Append element at end
numbers.append(50)
print("After append:", numbers)

# Insert at position
numbers.insert(1, 15)
print("After insert:", numbers)

# Extend array
numbers.extend([60, 70])
print("After extend:", numbers)

# Remove first occurrence of a value
numbers.remove(20)
print("After remove:", numbers)

# Find index BEFORE popping
if 30 in numbers:
    print("Index of 30:", numbers.index(30))
else:
    print("30 not found in array")

# Pop element at index 2
popped = numbers.pop(2)
print("Popped element:", popped)
print("After pop:", numbers)

# Count occurrences
print("Count of 10:", numbers.count(10))

# Reverse array
numbers.reverse()
print("After reverse:", numbers)

# Buffer info (memory address, length)
print("Buffer info:", numbers.buffer_info())

# Type code of array
print("Type code:", numbers.typecode)

# Size of each item in bytes
print("Item size:", numbers.itemsize)
