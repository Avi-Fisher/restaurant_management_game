from staff_members.Staff_base import Staff_base
from customers_and_orders.Order import Order


class Waiter(Staff_base):

    num_order = 1000

    def __init__(self,name,salary):

        super().__init__(name,salary)
        self.attribute = 0
        self.tip = 0

    def take_order(self,customer,menu):

        Waiter.num_order += 1
        order = Order(customer,Waiter.num_order)
        order.add_item(menu)

        return order

    def server_order(self,order):

        order.status = "delivered"
        order.customer.is_happy()

    def receive_tip(self,amount):

        self.tip += amount


    def get_total_earnings(self):

        return self.salary + self.tip
















