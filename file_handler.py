import json

from product import Product
from inventory import Inventory


def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            product = Product(
                item["id"],
                item["name"],
                item["price"],
                item["stock"]
            )
            inventory.add_product(product)

        print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("No inventory file found. Starting with an empty inventory.")

    return inventory


def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory.to_list(), file, indent=4)

    print("Inventory saved successfully.")


if __name__ == "__main__":
    inventory = load_inventory()
    inventory.display_all()