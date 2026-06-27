name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

total = maths + science + english
percentage = total / 3

print("\nMarksheet")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
