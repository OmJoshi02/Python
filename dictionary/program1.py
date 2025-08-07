d = {"a":1, "b":2,"c":3}

print(d.get("a"))
print(d.get("b"))

print(d.keys())
print(d.values())
print(d.items())

d.update({"d":4})
print(d)

d.pop("b")

d.popitem()
print(d)

copy_dict = d.copy()
print(copy_dict)

print(len(d))

d.clear()
print(d)
