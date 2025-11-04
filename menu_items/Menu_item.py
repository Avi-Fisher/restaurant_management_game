
class Menu_item():

    def __init__(self,name,price,category):

        self.name = name
        self.price = price
        self.category = category
        self.available = True


    def get_info(self):
        return f"Name: {self.name}, Price: {self.price}, Category: {self.category}"


    def set_available(self,status):
        self.available = status


    def is_available(self):
        return self.available











































