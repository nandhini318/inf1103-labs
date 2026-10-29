from file_handler import load_inventory, save_inventory
from product import Product


def main():
    inventory = load_inventory()

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Save and Exit")

        option = input("Enter option: ").strip()

        if option == "1":
            inventory.display_all()
               
        elif option == "2":
            product_id = input("Product ID: ").strip().upper()

            if not product_id:
                print("Product ID cannot be empty.")
                continue

            if inventory.search_product(product_id) is not None:
                print("Product ID already exists.")
                continue

            name = input("Product Name: ").strip()

            if not name:
                print("Product name cannot be empty.")
                continue

            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: "))
            except ValueError:
                print("Price must be a number and stock a whole number.")
                continue

            if price < 0 or stock < 0:
                print("Price and stock cannot be negative.")
                continue

            product = Product(product_id, name, price, stock)
            inventory.add_product(product)
            print("Product added successfully!")
               
        elif option == "3":
            product_id = input("Enter Product ID: ").strip().upper()
            product = inventory.search_product(product_id)

            if product is None:
                print("Product not found.")
            else:
                product.display_information()

                try:
                    quantity = int(input("New Stock Quantity: "))
                except ValueError:
                    print("Stock must be a whole number.")
                    continue

                product.update_stock(quantity)

        elif option == "4":
            product_id = input("Enter Product ID: ").strip().upper()
            product = inventory.search_product(product_id)

            if product is None:
                print("Product not found.")
            else:
                product.display_information()

        elif option == "5":
            save_inventory(inventory)
                
        elif option == "6":
            save_inventory(inventory)
            print("Goodbye!")


            break

        else:
            print("Invalid option. Choose a number from 1 to 6.")


if __name__ == "__main__":
    main()