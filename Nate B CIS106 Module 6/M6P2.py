partNumber = input("Enter part number: ")
quantity = int(input("Enter quantity: "))

if partNumber == "10" or partNumber == "55":
    unitCost = 1.00
elif partNumber == "99":
    unitCost = 2.00
elif partNumber == "80" or partNumber == "70":
    unitCost = 3.00
else:
    unitCost = 5.00

totalCost = quantity * unitCost

print(f"Part Number:     {partNumber:>10}")
print(f"Cost Per Unit:  ${unitCost:>10.2f}")
print(f"Total Cost:     ${totalCost:>10.2f}")

input("\nPress Enter to exit...")
