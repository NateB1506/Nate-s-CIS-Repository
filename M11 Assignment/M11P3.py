def calculateSalesMetrics(sales):
  if sales > 100000:
    commission = sales * 0.10
  else:
    commission = sales * 0.05

  nextYearTarget = sales * 0.05
  return commission, nextYearTarget


def main():
  salespersonName = input("Enter salesperson's last name: ")
  sales = float(input("Enter total sales: "))

  commission, nextYearTarget = calculateSalesMetrics(sales)

  print(f"\nSalesperson: {salespersonName}")
  print(f"Commission: ${commission:.2f}")
  print(f"Next Year's Target: ${nextYearTarget:.2f}")

  input("\nPress Enter to exit...")


if __name__ == "__main__":
  main()
