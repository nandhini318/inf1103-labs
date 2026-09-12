inventory = 0
rejected_entries = 0

while True:
    quantity = input("Enter stock quantity, or type quit: ")

    if quantity == "quit":
        break

    if not quantity.isdigit():
        print("Invalid input. Enter a non-negative whole number.")
        rejected_entries += 1
        continue

    quantity = int(quantity)
    inventory += quantity
    print("Current inventory:", inventory)
    if inventory > 500:
        print("Overstock alert! Inventory exceeds 500 units.")
        break
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", rejected_entries)