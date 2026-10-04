lastName = input("Enter employee last name: ")
salary = float(input("Enter salary: "))
jobLevel = int(input("Enter job level: "))

if jobLevel >= 10:
    bonusRate = 0.25
elif jobLevel >= 5:
    bonusRate = 0.20
else:
    bonusRate = 0.10

bonus = salary * bonusRate

print(f"Last Name: {lastName:>15}")
print(f"Bonus:    ${bonus:>15.2f}")

input("\nPress Enter to exit...")
