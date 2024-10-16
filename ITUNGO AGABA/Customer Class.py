class Customer:
    def __init__(self, name, address):
        self.name = name  
        self.address = address  

    def getName(self):
        return self.name  

    def getAddress(self):
        return self.address  

    def toString(self):
        return f"Customer Name: {self.name}, Address: {self.address}"  

