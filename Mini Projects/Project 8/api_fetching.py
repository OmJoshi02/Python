from operator import index

import requests
import json

url = "https://randomuser.me/api/?results=5"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("API data fetched successfully")

    print(json.dumps(data, indent = 4))

    users = []
    for user in data["results"]:
        users.append({
            "name": f"{user['name']['first']} {user['name']['last']}",
            "email" : f"{user['email']}"
        })

    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

    print("/n Processed user data and saved to users.json")

else:
    print(f"Error: unable to fetch data from {url} status code: {response.status_code}")