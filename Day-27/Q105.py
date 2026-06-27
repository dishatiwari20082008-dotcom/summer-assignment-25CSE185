students = {}

name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = int(input("Enter marks: "))

students[roll] = {
    "Name": name,
    "Marks": marks
}

print("\nStudent Record:")
print("Roll No:", roll)
print("Name:", students[roll]["Name"])
print("Marks:", students[roll]["Marks"])
