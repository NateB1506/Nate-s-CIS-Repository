class Student:
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        if self.district_code == "I":
            rate = 250.00
        else:
            rate = 500.00
        return self.enrolled_credits * rate


student_1 = Student("Jane", "Smith", "I", 12)
student_2 = Student("Mark", "Taylor", "O", 15)

print(f"Student: {student_1.first_name} {student_1.last_name}")
print(f"District Code: {student_1.district_code} | Credits: {student_1.enrolled_credits}")
print(f"Tuition Owed: ${student_1.compute_tuition():,.2f}\n")

print(f"Student: {student_2.first_name} {student_2.last_name}")
print(f"District Code: {student_2.district_code} | Credits: {student_2.enrolled_credits}")
print(f"Tuition Owed: ${student_2.compute_tuition():,.2f}")

input("\nPress Enter to exit...")
