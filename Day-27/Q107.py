name = input("Enter employee name: ")
basic = int(input("Enter basic salary: "))

hra = basic * 0.20
da = basic * 0.10

salary = basic + hra + da

print("\nSalary Details")
print("Employee Name:", name)
print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("Total Salary:", salary)
