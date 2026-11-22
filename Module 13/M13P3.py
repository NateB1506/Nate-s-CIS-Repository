import os

def printBattingAverages(playersDict):
    print(f"{'Player Name':<15} {'Batting Average':>15}")
    print("-" * 31)
    for name, avg in playersDict.items():
        print(f"{name:<15} {avg:>15.3f}")

def main():
    playersDict = {}
    scriptFolder = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(scriptFolder, "players.txt")

    try:
        with open(filepath, "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    lastName = parts[0]
                    battingAvg = float(parts[1])
                    playersDict[lastName] = battingAvg

        printBattingAverages(playersDict)

    except FileNotFoundError:
        print(f"Error: 'players.txt' not found in {scriptFolder}.")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
