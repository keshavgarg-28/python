# Task1:
# You are given a list of student records as tuples:
# students = [
#     ("Anil", 78),
#     ("Ravi", 45),
#     ("Meena", 88),
#     ("Sita", 62),
#     ("Raj", 49)
# ]

# Tasks
# Create a dictionary where:
# key → student name
# value → "Pass" if marks ≥ 50 else "Fail"
# Count how many students passed and failed.

students = [
    ("Anil", 78),
    ("Ravi", 45),
    ("Meena", 88),
    ("Sita", 62),
    ("Raj", 49)
]
result=dict(students)
print(result)
passcount=0
failcount=0
for k,v in result.items():
    if v>=50:
        result[k]="Pass"
        passcount=passcount+1
    else:
        result[k]="Fail"
        failcount=failcount+1
print(result)
print("Passed Students:",passcount, " Failed Student:",failcount)