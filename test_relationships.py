from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


supplier = Supplier("S001", "Tech Supplies", "sales@example.com")

laptop = PhysicalProduct(
    "P001", "Laptop", 1200.00, 15, 2.5, supplier
)

software = DigitalProduct(
    "D001", "Photo Editor", 49.99, 100, 500, supplier
)

del supplier  # Removes this variable name, not the products' references

laptop.supplier.display_information()
software.supplier.display_information()

print(laptop.supplier is software.supplier)  # Checks for the same object

print("\n--- Aggregation test ---")

inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(laptop)        # Adds laptop to Inventory A
inventory_a.remove_product("P001")     # Removes laptop from Inventory A

print("Laptop after removal:")
laptop.display_information()  # Still usable outside Inventory A

inventory_b.add_product(laptop)       # Adds laptop to Inventory B

print("Inventory B:")
inventory_b.display_all()

print(inventory_a.find_product("P001"))  # Should be None
print(inventory_b.find_product("P001") is laptop)  # Same object?