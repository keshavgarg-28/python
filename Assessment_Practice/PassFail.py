# "Task1:
# You are given a list of student records as tuples:
# students = [
#     (""Anil"", 78),
#     (""Ravi"", 45),
#     (""Meena"", 88),
#     (""Sita"", 62),
#     (""Raj"", 49)
# ]
# Tasks
# Create a dictionary where:
# key → student name
# value → ""Pass"" if marks ≥ 50 else ""Fail""
# Count how many students passed and failed.
students = [
    ("Anil", 78),
    ("Ravi", 45),
    ("Meena", 88),
    ("Sita", 62),
    ("Raj", 49)
]
result=dict(students)
cntPass=0
cntFail=0
for k,v in result.items():
    if v>50:
        result[k]="Pass"
        cntPass+=1
    else:
        result[k]="Fail"
        cntFail+=1
print(result)
print("Student Passed:", cntPass)
print("Student FAil:", cntFail )
