import json

with open("data.json", 'r') as f:
    data = json.load(f)
    print("Original data : ")
    print(data)
    data["status"] = "processed"

with open("data.json", 'w') as f:
    json.dump(data, f, indent=4)
