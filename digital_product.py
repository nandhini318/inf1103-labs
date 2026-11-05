from product import Product


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data
    
    def get_fulfilment_info(self):
        return "This product is delivered digitally."
    
    def display_information(self):
        super().display_information()
        print(f"Download size: {self.__download_size} MB")


if __name__ == "__main__":
    software = DigitalProduct("D001", "Photo Editor", 49.99, 100, 500)
    software.display_information()
    print(software.get_fulfilment_info())
    print(software.to_dict())