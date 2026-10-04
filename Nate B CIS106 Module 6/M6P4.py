tickets = int(input("Enter number of concert tickets: "))

if tickets >= 25:
    pricePerTicket = 50.00
elif tickets >= 10:
    pricePerTicket = 60.00
elif tickets >= 5:
    pricePerTicket = 70.00
else:
    pricePerTicket = 75.00

totalCost = tickets * pricePerTicket

print(f"Number of Tickets: {tickets:>10}")
print(f"Price Per Ticket: ${pricePerTicket:>10.2f}")
print(f"Total Cost:       ${totalCost:>10.2f}")

input("\nPress Enter to exit...")
