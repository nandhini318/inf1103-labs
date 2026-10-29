from product import Product


class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def to_list(self):
        data = []

        for product in self.__products:
            data.append(product.to_dict())

        return data

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return

        for product in self.__products:
            product.display_information()


if __name__ == "__main__":
    inventory = Inventory()

    product1 = Product("P001", "Laptop", 1200.00, 15)
    product2 = Product("P002", "Mouse", 25.50, 40)

    inventory.add_product(product1)
    inventory.add_product(product2)

    print(inventory.to_list())