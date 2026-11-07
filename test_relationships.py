from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


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