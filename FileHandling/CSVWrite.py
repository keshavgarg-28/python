import csv
# with open("data.csv","w",newline="") as f:
#     writer=csv.writer(f)
#     writer.writerow(["name", "age", "city"])

with open("data.csv","w", newline="") as f:
    names=["name", "age","city"]
    writer=csv.DictWriter(f, fieldnames=names)
    writer.writeheader()
    writer.writerow({"name":"Alice", "age":30, "city":"Delhi"})
