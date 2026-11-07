from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        weight: float,
        supplier: Supplier
    ) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = weight
    
    def to_dict(self) -> dict[str, object]:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data
    
    def calculate_shipping_cost(self) -> float:
        return self.__weight * 5
    
    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."
    
    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")


