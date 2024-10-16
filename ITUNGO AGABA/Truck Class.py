class Vehicle:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def toString(self):
        return f"This vehicle is {self.color}"

class Truck(Vehicle):
    def __init__(self, color, trailer=False):
        super().__init__(color)  
        self.trailer = trailer  

    def toString(self):
        base_string = super().toString()
        return f"{base_string}\nHas trailer: {self.trailer}"

