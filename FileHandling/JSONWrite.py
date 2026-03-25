import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "Mumbai"
}

with open("data.json", "w") as f:
    json.dump(data, f)