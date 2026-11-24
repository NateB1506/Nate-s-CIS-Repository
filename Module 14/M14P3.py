class Student:
    tuition_rates = {
        "I": 250.00,
        "O": 500.00,
        "X": 800.00,
        "G": 250.00
    }

    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        rate = self.tuition_rates.get(self.district_code, 500.00)
        return self.enrolled_credits * rate


students = [
    Student("Jane", "Smith", "I", 12),
    Student("Mark", "Taylor", "O", 15),
    Student("Kenji", "Sato", "X", 12),
    Student("Elena", "Gomez", "G", 9)
]

for s in students:
    print(f"Student: {s.first_name} {s.last_name} | Code: {s.district_code} | Credits: {s.enrolled_credits} | Tuition Owed: ${s.compute_tuition():,.2f}")

input("\nPress Enter to exit...")
