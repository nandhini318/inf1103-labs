class Supplier:
    def __init__(
        self,
        supplier_id: str,
        name: str,
        contact_email: str
    ) -> None:
        self.supplier_id: str = supplier_id
        self.name: str = name
        self.contact_email: str = contact_email

    def to_dict(self) -> dict[str, str]:    #returns the supplier’s details as a dictionary. dict[str, str] means its keys and values are strings.
        return {
            "supplier_id": self.supplier_id,
            "name": self.name,
            "contact_email": self.contact_email
        }
    
    def display_information(self) -> None:
        print(
            f"Supplier ID: {self.supplier_id} | "
            f"Name: {self.name} | "
            f"Email: {self.contact_email}"
        )


if __name__ == "__main__":
    supplier = Supplier("S001", "Tech Supplies", "sales@example.com")
    supplier.display_information()