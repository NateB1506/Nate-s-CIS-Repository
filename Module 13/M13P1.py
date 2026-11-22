def main():
    studentGrades = {
        "Alice": 92,
        "Bob": 85,
        "Charlie": 78,
        "Diana": 95,
        "Evan": 88
    }

    print(f"{'Student Name':<15} {'Grade':>10}")
    print("-" * 26)

    total = 0
    for name, grade in studentGrades.items():
        print(f"{name:<15} {grade:>10}")
        total += grade

    classAverage = total / len(studentGrades)
    print("-" * 26)
    print(f"{'Class Average':<15} {classAverage:>10.2f}")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
