
class Staff_base():

    def __init__(self,name,salary):

        self.name = name
        self.salary = salary
        self.energy = 100


    def work(self):

        self.energy -= 10
        print(f"{self.name} working now, energy: {self.energy}")


    def rest(self):

        self.salary += 20

        if self.salary > 100:
            self.salary = 100


    def is_tired(self):

        if self.energy < 30:
            return True


    def get_info(self):

        return f"name: {self.name}, role: {self.__class__.__name__}, salary: {self.salary}, Energy: {self.energy} "


















