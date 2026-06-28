tickets = 10

name = input("Enter passenger name: ")
quantity = int(input("Enter number of tickets: "))

if quantity <= tickets:
    tickets -= quantity
    print("\nTicket booked successfully")
    print("Passenger:", name)
    print("Tickets booked:", quantity)
    print("Remaining tickets:", tickets)
else:
    print("Tickets not available")
