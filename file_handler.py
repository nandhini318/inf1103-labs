import json

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from supplier import Supplier

def load_inventory() -> Inventory:
    inventory = Inventory()

    try:
        with open("inventory_week10.json", "r") as file:
            data = json.load(file)

        for item in data:
            supplier_data = item["supplier"]

            supplier = Supplier(
                supplier_data["supplier_id"],
                supplier_data["name"],
                supplier_data["contact_email"]
            )

            if item["type"] == "physical":
                product = PhysicalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["weight"],
                    supplier
                )

            elif item["type"] == "digital":
                product = DigitalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["download_size"],
                    supplier
                )

            else:
                raise ValueError("Unknown product type.")

            inventory.add_product(product)

        print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("No Week 10 file found. Starting with an empty inventory.")

    return inventory

def save_inventory(inventory: Inventory) -> None:
    with open("inventory_week10.json", "w") as file:
        json.dump(inventory.to_list(), file, indent=4)

    print("Inventory saved successfully.")


if __name__ == "__main__":
    inventory = load_inventory()
    save_inventory(inventory)

    reloaded_inventory = load_inventory()
    reloaded_inventory.display_all()