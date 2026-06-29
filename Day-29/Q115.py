string = input("Enter a string: ")

print("1. Reverse String")
print("2. Count Characters")
print("3. Convert Uppercase")
print("4. Convert Lowercase")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Reverse:", string[::-1])

elif choice == 2:
    print("Length:", len(string))

elif choice == 3:
    print("Uppercase:", string.upper())

elif choice == 4:
    print("Lowercase:", string.lower())

else:
    print("Invalid choice")
