from product import Product
from order_line import OrderLine


class Order:
    def __init__(self, order_id: str) -> None:
        self.order_id: str = order_id      #self.order_id stores its ID, such as "O001"
        self.order_lines: list[OrderLine] = []    #self.order_lines starts as an empty list. It will hold the rows of this order.
#list[OrderLine] is just a type hint saying the list is intended to contain OrderLine objects. It doesn’t create any lines yet.

    def add_order_line(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            print("Quantity must be positive.")
            return

        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)    #creates a new OrderLine object and adds it to the order_lines list.

    def calculate_total(self) -> float:
        total = 0.0

        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()    #OrderLine calculates one row’s subtotal & Order adds all the subtotals.

        return total

    def remove_order_line(self, index: int) -> None:
        if 0 <= index < len(self.order_lines):    #checks if the index is valid       
             self.order_lines.pop(index)        #removes the OrderLine at that index from the order_lines list
        else:
            print("Order line not found.")