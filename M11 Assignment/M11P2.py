def calculateExamStats(score1, score2, score3):
  totalPoints = score1 + score2 + score3
  averageScore = totalPoints / 3
  return totalPoints, averageScore


def main():
  lastName = input("Enter student's last name: ")
  score1 = float(input("Enter exam score 1: "))
  score2 = float(input("Enter exam score 2: "))
  score3 = float(input("Enter exam score 3: "))

  totalPoints, averageScore = calculateExamStats(score1, score2, score3)

  print(f"\nStudent Last Name: {lastName}")
  print(f"Total Points: {totalPoints:.2f}")
  print(f"Average Exam Score: {averageScore:.2f}")

  input("\nPress Enter to exit...")


if __name__ == "__main__":
  main()
