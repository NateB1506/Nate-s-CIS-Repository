quantity = int(input("Enter quantity of widgets: "))

if quantity > 10000:
    price = 10.00
elif quantity >= 5000:
    price = 20.00
else:
    price = 30.00

extendedPrice = quantity * price
taxAmount = extendedPrice * 0.07
total = extendedPrice + taxAmount

print(f"Extended Price: ${extendedPrice:>10.2f}")
print(f"Tax (7%):        ${taxAmount:>10.2f}")
print(f"Total:           ${total:>10.2f}")

input("\nPress Enter to exit...")
