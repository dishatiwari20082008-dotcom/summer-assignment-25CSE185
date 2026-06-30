students = []

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append([name, marks])
    print("Student added")

def display_students():
    print("\nStudent Records")
    for s in students:
        print("Name:", s[0], "Marks:", s[1])

def search_student():
    name = input("Enter name to search: ")
    
    for s in students:
        if s[0] == name:
            print("Found - Name:", s[0], "Marks:", s[1])
            return
    
    print("Student not found")


while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        break

    else:
        print("Invalid choice")
