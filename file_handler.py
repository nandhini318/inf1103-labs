import json

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

def load_inventory():
    inventory = Inventory()

    try:
        
        with open("inventory_week9.json", "r") as file:   
            data = json.load(file)

        for item in data:
            if item["type"] == "physical":
                product = PhysicalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["weight"]
                )

            elif item["type"] == "digital":
                product = DigitalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["download_size"]
                )

            else:
                raise ValueError("Unknown product type in inventory.json.")

            inventory.add_product(product)

        print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("inventory_week9.json not found. Starting with an empty inventory.")

    return inventory


def save_inventory(inventory):
    with open("inventory_week9.json", "w") as file:
        json.dump(inventory.to_list(), file, indent=4)

    print("Inventory saved successfully.")


if __name__ == "__main__":
    inventory = load_inventory()
    save_inventory(inventory)

    reloaded_inventory = load_inventory()
    reloaded_inventory.display_all()