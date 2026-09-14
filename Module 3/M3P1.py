ticker = input("Enter the stock ticker symbol: ")
shares = float(input("Enter the number of shares: "))
costPerShare = float(input("Enter the cost per share: "))

amountInvested = shares * costPerShare

print(f"Stock: {ticker} | Amount Invested: ${amountInvested:.2f}")

input("\nPress Enter to exit...")
