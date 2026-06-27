employees = {}

id = input("Enter employee ID: ")
name = input("Enter employee name: ")
department = input("Enter department: ")

employees[id] = {
    "Name": name,
    "Department": department
}

print("\nEmployee Record:")
print("Employee ID:", id)
print("Name:", employees[id]["Name"])
print("Department:", employees[id]["Department"])
