from menu_items.Menu_item import Menu_item

class Menu():

    def __init__(self):
        self.items = []


    def add_item(self,menu_item):
        self.items.append(menu_item)


    def remove_item(self,item_name):
        for i in self.items:
            if i.name == item_name:
                self.items.remove(i)


    def get_item_by_name(self,name):
        for i in self.items:
            if i.name == name:
               return i


    def get_items_by_category(self,category):
        list_category = []

        for i in self.items:
            if i.category == category:
                list_category.append(i)


    def display_menu(self):
        for i in self.items:
            print(i.get_info)


    def get_total_items(self):
        return len(self.items)