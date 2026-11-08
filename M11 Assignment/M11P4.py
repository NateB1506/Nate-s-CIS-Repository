def calculateBowlingStats(game1, game2, game3, handicap):
  totalScore = game1 + game2 + game3
  averageScore = totalScore / 3
  averageWithHandicap = averageScore + handicap
  return averageScore, averageWithHandicap


def main():
  lastName = input("Enter bowler's last name: ")
  game1 = float(input("Enter game 1 score: "))
  game2 = float(input("Enter game 2 score: "))
  game3 = float(input("Enter game 3 score: "))
  handicap = float(input("Enter handicap: "))

  averageScore, averageWithHandicap = calculateBowlingStats(
      game1, game2, game3, handicap
  )

  print(f"\nBowler Last Name: {lastName}")
  print(f"Average Score: {averageScore:.2f}")
  print(f"Average Score with Handicap: {averageWithHandicap:.2f}")

  input("\nPress Enter to exit...")


if __name__ == "__main__":
  main()
