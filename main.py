from customers_and_orders.Order import Order
from menu_items.Menu import Menu
from menu_items.Menu_item import Menu_item
from customers_and_orders.Customer import Customer


if __name__ == "__main__":

    m1 = Menu_item("tost",24,"brad")
    m2 = Menu_item("pizza",76,"pizza")
    m3 = Menu_item("pizza_white_onion", 43, "pizza")

    menu = Menu()
    menu.add_item(m1)
    menu.add_item(m2)
    menu.add_item(m3)

    c1 = Customer("Avi")
    c2 = Customer("David")
    c3 = Customer("Tamar")

    order = Order(c1,111)
    order.add_item(m1)
    order.add_item(m2)















