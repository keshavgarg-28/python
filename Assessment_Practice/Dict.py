# Task 1:

# You are given a list of strings in the following format:

# data = [
#     "id:1,name:john,skills:python|java|sql",
#     "id:2,name:sara,skills:python|aws",
#     "id:3,name:mike,skills:java|c++|docker",
# ]

# Task:
# Write a Python program to convert the above list into the following dictionary structure:

# {
#   1: {"name": "john", "skills": ["python", "java", "sql"]},
#   2: {"name": "sara", "skills": ["python", "aws"]},
#   3: {"name": "mike", "skills": ["java", "c++", "docker"]}
# }
data = [
     "id:1,name:john,skills:python|java|sql",
     "id:2,name:sara,skills:python|aws",
     "id:3,name:mike,skills:java|c++|docker",
]
d={}
for i in data:
    rec=i.split(",")
    id=int(rec[0].split(":")[1])
    name=rec[1].split(":")[1]
    skills=rec[2].split(":")[1].split("|")
    d[id]={
        "name": name,
        "skills":skills
    }
print(d)