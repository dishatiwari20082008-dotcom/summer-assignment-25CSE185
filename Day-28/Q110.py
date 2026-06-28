account = {}

acc_no = input("Enter account number: ")
name = input("Enter account holder name: ")
balance = int(input("Enter initial balance: "))

account[acc_no] = {
    "Name": name,
    "Balance": balance
}

print("\nBank Account Details")
print("Account Number:", acc_no)
print("Name:", account[acc_no]["Name"])
print("Balance:", account[acc_no]["Balance"])
