from staff_members.Staff_base import Staff_base

class Chef(Staff_base):

    def __init__(self,name,salary,specialty):

        super().__init__(name,salary)
        self.specialty = specialty


    def cook_order(self,order):

        if order.status == 'pending':
            order.status = "cooking"
            self.work()
        elif order.status == 'cooking':
            order.status = "ready"
            self.work()
        elif order.status == "cooking":
            order.status = "over cooking"
            self.energy -= 15
            if self.energy < 0:
                self.energy = 0






















