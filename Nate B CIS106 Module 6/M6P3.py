principle = float(input("Enter principle amount: "))
years = int(input("Enter years to maturity: "))

if principle > 100000 and years == 5:
    interestRate = 0.06
elif principle >= 50000 and principle <= 100000 and years == 10:
    interestRate = 0.05
elif principle >= 50000 and principle <= 100000 and years == 5:
    interestRate = 0.04
else:
    interestRate = 0.02

interestAmount = principle * interestRate

print(f"Principle:        ${principle:>10.2f}")
print(f"Interest Rate:     {interestRate * 100:>9.0f}%")
print(f"First Year Interest: ${interestAmount:>8.2f}")

input("\nPress Enter to exit...")
