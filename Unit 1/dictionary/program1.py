d = {"a":1, "b":2,"c":3}

print(d.get("a")) #returns value for a
print(d.get("b"))

print(d.keys()) #returns all keys
print(d.values()) #return all values
print(d.items()) #return all key:value pairs

d.update({"d":4}) #adds key d with value 4
print(d)

d.pop("b") #removes key b

d.popitem() #removes last inserted item
print(d)

copy_dict = d.copy() #copies from 1 dictionary to another
print(copy_dict)

print(len(d)) #returns length of dictionary

d.clear() #clears the dictionary
print(d)
