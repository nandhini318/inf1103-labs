class Product:
    def __init__(self, product_id, name, price, stock):      #a special method that sets up a new object. initializes the attributes of the class
        self.__product_id = product_id          #a private attribute that stores the product ID
        self.__name = name
        self.__price = price
        self.__stock = stock

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }
    
    def get_product_id(self):
        return self.__product_id
    
    def update_stock(self, quantity):
        if quantity < 0:
            print("Stock cannot be negative.")
            return

        self.__stock = quantity
        print("Stock updated successfully!")
    
    def display_information(self):           #a method to display the product information in a formatted manner
        print(
            f"ID: {self.__product_id} | Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | Stock: {self.__stock}"
        )

if __name__ == "__main__":
    product1 = Product("P001", "Laptop", 1200.00, 15)
    product2 = Product("P002", "Mouse", 25.50, 40)

    product1.update_stock(-5)
    product1.display_information()
    product2.display_information()