from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from product import Product
from file_handler import save_inventory, load_inventory

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
print(inventory_b.find_product("P001") is laptop)  #True 


print("\n--- Composition test ---")

order_a = Order("O001")
order_b = Order("O002")

order_a.add_order_line(laptop, 2)
order_b.add_order_line(laptop, 1)

print("Lines in Order A:", len(order_a.order_lines))
print("Lines in Order B:", len(order_b.order_lines))

print(
    "Same OrderLine?",
    order_a.order_lines[0] is order_b.order_lines[0]
)

print(
    "Same Product?",
    order_a.order_lines[0].product is order_b.order_lines[0].product
)

print("Order A total:", order_a.calculate_total())
print("Order B total:", order_b.calculate_total())





order_a.add_order_line(software, 1)

print("\nOrder A lines:")
for line in order_a.order_lines:
    print(
        f"Product: {line.product.get_product_id()} | "
        f"Quantity: {line.quantity} | "
        f"Subtotal: ${line.calculate_subtotal():.2f}"
    )

print(f"Total before removal: ${order_a.calculate_total():.2f}")

order_a.remove_order_line(0)  # Removes the Laptop row from this order

print(f"Total after removal: ${order_a.calculate_total():.2f}")

print("Laptop still exists:")
laptop.display_information()




def show_product_details(product: Product) -> None:     #liscov substitution principle - a function that expects a Product can also accept PhysicalProduct or DigitalProduct.
    product.display_information()
    print(product.get_fulfilment_info())


print("\n--- LSP and polymorphism test ---")

show_product_details(laptop)
show_product_details(software)





print("\n--- Mixed inventory polymorphism test ---")

mixed_inventory = Inventory()
mixed_inventory.add_product(laptop)
mixed_inventory.add_product(software)

mixed_inventory.display_all()

for product_id in ("P001", "D001"):
    product = mixed_inventory.find_product(product_id)

    if product is not None:
        print(product.get_fulfilment_info())






print("\n--- Week 10 persistence test ---")

save_inventory(mixed_inventory)

loaded_inventory = load_inventory()
loaded_inventory.display_all()

loaded_laptop = loaded_inventory.find_product("P001")

if loaded_laptop is not None:
    print("Reloaded Laptop supplier:")
    loaded_laptop.supplier.display_information()