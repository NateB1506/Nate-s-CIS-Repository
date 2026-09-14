make = input("Enter auto make: ")
model = input("Enter auto model: ")
msrp = float(input("Enter MSRP amount: "))
discountPercent = float(input("Enter discount percent as a decimal (e.g., 0.15 for 15%): "))

amountOff = msrp * discountPercent
discountedPrice = msrp - amountOff

print(f"Vehicle: {make} {model} | MSRP: ${msrp:.2f} | Discount: {discountPercent * 100:.1f}% | Amount Off: ${amountOff:.2f} | Final Price: ${discountedPrice:.2f}")

input("\nPress Enter to exit...")
