
class Order():

    def __init__(self,customer,order_number):

        self.customer = customer.name
        self.order_number = order_number
        self.items = []
        self.status = "pending"
        self.total_price = 0


    def add_item(self,menu_item):

        self.items.append(menu_item.get_info())
        self.total_price += menu_item.price


    def remove_item(self,menu_item):

        self.items.remove(menu_item.get_info())


    def get_total(self):
        return self.total_price


    def set_status(self,new_status):

        self.status = new_status


    def display_order(self):

        print(f"Order_number: {self.order_number}, Customer: {self.customer}, items: {self.items}, Total_price: {self.total_price}, status: {self.status}")


    def is_complete(self):

        if self.status == 'delivered':
            return True












































