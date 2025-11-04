

class Customer():

    def __init__(self,name):

        self.name = name
        self.satisfaction = 50


    def increase_satisfaction(self,amount):
        if self.satisfaction + amount <= 100:
            self.satisfaction += amount


    def decrease_satisfaction(self,amount):
        if (self.satisfaction - amount) >= 0:
            self.satisfaction -= amount


    def is_happy(self):
        if self.satisfaction > 70:
            return True


    def get_info(self):
        return f"Customer: {self.name} satisfaction: {self.satisfaction}"

















