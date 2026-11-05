from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data
    
    def calculate_shipping_cost(self):
        return self.__weight * 5
    
    def get_fulfilment_info(self):
        return "This product requires physical shipping."
    
    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")


if __name__ == "__main__":
    laptop = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.5)
    laptop.display_information()
    print(f"Shipping cost: ${laptop.calculate_shipping_cost():.2f}")

    mouse = PhysicalProduct("P002", "Mouse", 25.50, 40, 0.2)
    print(f"Mouse shipping: ${mouse.calculate_shipping_cost():.2f}")

    print(laptop.get_fulfilment_info())
    print(laptop.to_dict())