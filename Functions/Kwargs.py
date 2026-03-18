def student_Info(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
student_Info(name="John", age=22, marks=90)