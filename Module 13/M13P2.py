def calculateClassAverages(gradesDict):
    numStudents = len(gradesDict)
    numGrades = 3
    classAverages = []

    for i in range(numGrades):
        totalForGrade = sum(grades[i] for grades in gradesDict.values())
        classAverages.append(totalForGrade / numStudents)

    return classAverages

def main():
    studentGrades = {
        "Alice": [92, 88, 95],
        "Bob": [85, 80, 84],
        "Charlie": [78, 82, 79],
        "Diana": [95, 96, 94],
        "Evan": [88, 85, 90]
    }

    print("=== Student Grade Averages ===")
    print(f"{'Student':<12} {'Grades':<18} {'Average':>8}")
    print("-" * 40)
    for name, grades in studentGrades.items():
        gradesStr = ", ".join(str(g) for g in grades)
        studentAvg = sum(grades) / len(grades)
        print(f"{name:<12} {gradesStr:<18} {studentAvg:>8.2f}")

    classAverages = calculateClassAverages(studentGrades)

    print("\n=== Class Averages by Grade ===")
    print(f"{'Grade Item':<12} {'Class Average':>14}")
    print("-" * 28)
    for index, avg in enumerate(classAverages, start=1):
        print(f"Grade {index:<6} {avg:>14.2f}")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
