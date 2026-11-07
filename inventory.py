from product import Product


class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = []     #a type hint - list[Product] allows both physical and digital products.
    
    def add_product(self, product: Product) -> None:    
        self.__products.append(product)

    def find_product(self, product_id: str) -> Product | None:     #Product|None means the method returns a Product, or None if not found.
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)

        if product is None:
            print("Product not found.")
            return

        self.__products.remove(product)                #.remove(product) removes the reference from the inventory list
        print("Product removed from inventory.")    
    
    def search_product(self, product_id: str) -> Product | None:
        return self.find_product(product_id)

    

    def to_list(self) -> list[dict[str, object]]:
        data: list[dict[str, object]] = []

        for product in self.__products:
            data.append(product.to_dict())

        return data

    def display_all(self) -> None:       
        if not self.__products:
            print("Inventory is empty.")
            return

        for product in self.__products:
            product.display_information()


