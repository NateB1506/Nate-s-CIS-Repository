lastName = input("Enter student last name: ")
midterm = float(input("Enter midterm exam score (0-100): "))
finalExam = float(input("Enter final exam score (0-100): "))

totalExamPoints = (0.40 * midterm) + (0.60 * finalExam)

print(f"Student: {lastName} | Total Exam Points: {totalExamPoints:.2f}")

input("\nPress Enter to exit...")
