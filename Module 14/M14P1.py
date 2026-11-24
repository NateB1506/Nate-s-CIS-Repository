class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = first.lower() + "." + last.lower() + "@company.com"
        self.salary = salary

    def fullname(self):
        return f"{self.first} {self.last}"

    def compute_bonus(self, bonus_rate):
        return self.salary * bonus_rate


emp_1 = Employee("Nate", "Bultron", 60000)

print("Employee:", emp_1.fullname())
print("Email:", emp_1.email)
print(f"Base Salary: ${emp_1.salary:,.2f}")

rate = float(input("Enter the bonus rate (e.g., 0.10 for 10%): "))
bonus = emp_1.compute_bonus(rate)

print(f"Bonus Amount: ${bonus:,.2f}")

input("\nPress Enter to exit...")
