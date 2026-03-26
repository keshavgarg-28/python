import csv
import json

data = []

with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)