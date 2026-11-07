from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):    #an abstract base class that defines the common attributes and methods for all products
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        supplier: Supplier
    ) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.supplier: Supplier = supplier
    
    @abstractmethod
    def get_fulfilment_info(self):
        pass
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