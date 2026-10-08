import json

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)            #load the inventory from the JSON file into python data structure (list of dictionaries)

        print("Inventory loaded successfully.")
        return inventory

    except FileNotFoundError:
        print("inventory.json not found. Starting with an empty inventory.")
        return []

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json.")
    
def search_product(inventory, product_id):
    for product in inventory:
        if product["id"] == product_id:
            return product

    return None               #none means product not found

def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip().upper()     #.strip() removes spaces at the beginning and end  and .upper() turns an ID such as p004 into P004

    if not product_id:
        print("Product ID cannot be empty.")
        return

    if search_product(inventory, product_id) is not None:         #make sure no duplicate
        print("Product ID already exists.")
        return

    name = input("Product Name: ").strip()

    if not name:
        print("Product name cannot be empty.")
        return

    try:
        price = float(input("Price: "))                    #error handling for invalid price input
        stock = int(input("Stock Quantity: "))             #error handling for invalid stock input
    except ValueError:
        print("Price must be a number and stock must be a whole number.")    #error handling for invalid input
        return

    if price < 0 or stock < 0:
        print("Price and stock cannot be negative.")
        return

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(product)
    print("Product added successfully!")

def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip().upper()
    product = search_product(inventory, product_id)                   # Search for the product

    if product is None:
        print("Product not found.")
        return

    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")       #auto display the current stock of the product before updating it

    try:
        new_stock = int(input("New Stock Quantity: "))
    except ValueError:
        print("Stock must be a whole number.")
        return

    if new_stock < 0:
        print("Stock cannot be negative.")
        return

    product["stock"] = new_stock                      #auto update the stock of the product in the inventory without doing addition
    print("Stock updated successfully!")    

def display_all(inventory):
    if not inventory:
        print("Inventory is empty.")
        return

    print("\nCurrent Inventory")
    print("-" * 60)

    for product in inventory:             #use loop to print all
        print(
            f"ID: {product['id']} | Name: {product['name']} | "         #The f makes it an f-string: a string that inserts the values of variables or expressions placed inside {}       
            f"Price: ${product['price']:.2f} | Stock: {product['stock']}"
        )

    print("-" * 60)

inventory = load_inventory()
display_all(inventory)

