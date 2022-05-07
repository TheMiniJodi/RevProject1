class Coffee:

    def __init__(self,coffeeId, name, pricePerLB, roasting, quantity):
        self.coffeeId = coffeeId
        self.name = name
        self.pricePerLB = pricePerLB
        self.roasting = roasting
        self.quantity = quantity

    def __str__(self):
        return ('Coffee item has been added:\n----------------------------\n'+
        'ID: {self.coffeeId}\nName: {self.name}\n'.format(self=self)+
        'Price Per Pound: {self.pricePerLB}\nRoasting Type: {self.roasting}\n'.format(self=self)+
        'Quantity: {self.quantity}'.format(self=self))

