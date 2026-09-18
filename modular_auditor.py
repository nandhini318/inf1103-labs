def calculate_tax(amount):
    return amount * 0.10
def process_delivery(current_total, new_value):
    return current_total + new_value
def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)
def get_valid_input():
    failed_attempts = 0

    while True:
        quantity = input("Enter stock quantity, or type quit: ")

        if quantity == "quit":
            return "quit", failed_attempts

        if not quantity.isdigit():
            print("Invalid input. Enter a non-negative whole number.")
            failed_attempts += 1
            continue

        return int(quantity), failed_attempts
inventory = 0
rejected_entries = 0

while True:
    quantity, failed_attempts = get_valid_input()
    rejected_entries += failed_attempts

    if quantity == "quit":
        break

    inventory = process_delivery(inventory, quantity)
    tax = calculate_tax(quantity)
    print("Tax for this delivery:", tax)
    print("Current inventory:", inventory)

    if inventory > 500:
        print("Overstock alert! Inventory exceeds 500 units.")
        break

generate_report(inventory, rejected_entries)