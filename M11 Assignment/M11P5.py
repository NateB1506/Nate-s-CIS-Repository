total = 0.0
tax = 0.0


def computeTotals(quantity, unitPrice):
  global total, tax
  subtotal = quantity * unitPrice
  tax = subtotal * 0.07
  total = subtotal + tax


def main():
  global total, tax
  quantity = int(input("Enter item quantity: "))
  unitPrice = float(input("Enter unit price: "))

  computeTotals(quantity, unitPrice)

  print(f"\nTotal (including 7% tax): ${total:.2f}")
  print(f"Tax Amount: ${tax:.2f}")

  input("\nPress Enter to exit...")


if __name__ == "__main__":
  main()
