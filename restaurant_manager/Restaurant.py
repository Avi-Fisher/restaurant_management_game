from

from menu_items.Menu import Menu


class Restaurant():

    def __init__(self,name):

        self.name =name
        self.menu = Menu
        self.staff = []
        self.orders = []
        self.money = 1000


    def hire_staff(self,staff_member):
        self.staff.append(staff_member)

    def fire_staff(self,staff_name):

        for i in self.staff:
            if i.name == staff_name:
                self.staff.remove(i)
                break


    def create_order(self,customer):






























