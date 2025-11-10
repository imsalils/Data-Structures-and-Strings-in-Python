student={"Alice":90,"salil":99,"Dev":98,"yash":99,"astha":95}
name=input("Enter the student's name:")
if name in student.keys():
    print(f"{name}'s marks: {student[name]}")
else:
    print("student not found")