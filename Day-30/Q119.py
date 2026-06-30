employees = []

n = int(input("Enter number of employees: "))

for i in range(n):
    name = input("Enter employee name: ")
    salary = int(input("Enter salary: "))
    
    employees.append([name, salary])

print("\nEmployee Records")

for emp in employees:
    print("Name:", emp[0], "Salary:", emp[1])
