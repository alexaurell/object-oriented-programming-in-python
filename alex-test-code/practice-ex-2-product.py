class Product:
    def __init__(self, id, marked_price, discount):
        self._id = id
        self._marked_price = marked_price
        self._discount = discount
    
    def display(self):
        print(self._id, self._marked_price, self._discount)

    @property
    def selling_price(self):
        return self._marked_price*(1 - 0.01*self._discount)

    @property
    def discount(self):
        return self._discount+2 if self._marked_price > 500 else self._discount

    @discount.setter
    def discount(self, val):
        self._discount = val
    #@discount.setter
    #def discount(self, val):
    #    if self._marked_price > 500:
    #        self._discount = self._discount + 2

p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)

#p4.discount = 10
p4.display()
print(p4._id, p4.selling_price)