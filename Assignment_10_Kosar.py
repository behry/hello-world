class item:
    def __init__(self,item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
    def purchase(self):
        return self.quantity * self.price

class customer:
    def __init__(self, customer_id, phone_number):
        self.customer_id = customer_id
        self.phone_number = phone_number


cst = customer(2778, 15645512)
it = item('Pencil', 15, 3)
print(it.purchase())

