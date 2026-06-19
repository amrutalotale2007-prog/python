students = {
    "Amit": 85,
    "Neha": 92,
    "Riya": 78,
    "Rahul": 88,
    "Priya": 95
}


for name, marks in students.items():
    print(name, ":", marks)

avg = sum(students.values()) / len(students)
print("Class Average:", avg)


topper = max(students, key=students.get)
print("Highest Marks:", topper, "-", students[topper])
