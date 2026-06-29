inventory = {}

item = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = int(input("Enter price: "))

inventory[item] = {
    "Quantity": quantity,
    "Price": price
}

print("\nInventory Details")

print("Item:", item)
print("Quantity:", inventory[item]["Quantity"])
print("Price:", inventory[item]["Price"])
