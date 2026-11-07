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
    def get_fulfilment_info(self) -> str:
        pass
    
    def to_dict(self) -> dict[str, object]:
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.supplier.to_dict()      #nested dictionary to include supplier details
        }
    
    @property
    def price(self) -> float:
        return self.__price

    def get_product_id(self) -> str:
        return self.__product_id
    
    def update_stock(self, quantity: int) -> None:
        if quantity < 0:
            print("Stock cannot be negative.")
            return

        self.__stock = quantity
        print("Stock updated successfully!")
    
    def display_information(self) -> None:           #a method to display the product information in a formatted manner
        print(
            f"ID: {self.__product_id} | Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | Stock: {self.__stock}"
        )
