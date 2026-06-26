balance = 10000

print("1. Check Balance")
print("2. Withdraw Money")
print("3. Deposit Money")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Balance:", balance)

elif choice == 2:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance -= amount
        print("Please collect your cash")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")

elif choice == 3:
    amount = int(input("Enter deposit amount: "))
    balance += amount
    print("Updated balance:", balance)

else:
    print("Invalid choice")
