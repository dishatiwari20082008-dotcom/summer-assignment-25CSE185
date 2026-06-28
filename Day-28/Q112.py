contacts = {}

name = input("Enter contact name: ")
phone = input("Enter phone number: ")

contacts[name] = phone

print("\nContact Details")
print("Name:", name)
print("Phone:", contacts[name])
