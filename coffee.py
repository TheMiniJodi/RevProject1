# This is a coffee class 

class Coffee:

    def __init__(self,coffeeId, name, pricePerLB, roasting, quantity):
        self.coffeeId = coffeeId
        self.name = name
        self.pricePerLB = pricePerLB
        self.roasting = roasting
        self.quantity = quantity

    def __str__(self):
        return ('Coffee item has been added\nName: {self.name}\nPrice Per Pound: {self.pricePerLB}\nRoasting Type: {self.roasting}\nQuantity: {self.quantity}'.format(self=self))

