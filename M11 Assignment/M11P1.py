def calculateDiscount(quantity, price, discountRate):
  discountAmount = (quantity * price) * discountRate
  discountedPrice = (quantity * price) - discountAmount
  return discountAmount, discountedPrice


def main():
  quantity = int(input("Enter quantity: "))
  price = float(input("Enter unit price: "))
  discountRate = float(input("Enter discount rate (ex. 0.15 for 15%): "))

  discountAmount, discountedPrice = calculateDiscount(
      quantity, price, discountRate
  )

  print("\n--- Order Summary ---")
  print("Quantity:", quantity)
  print(f"Price: ${price:.2f}")
  print(f"Discount Amount: ${discountAmount:.2f}")
  print(f"Discounted Price: ${discountedPrice:.2f}")

  input("\nPress Enter to exit...")


if __name__ == "__main__":
  main()
