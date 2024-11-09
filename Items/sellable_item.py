from Items.Item import Item


class SellableItem(Item):
    price: float
    stock_amount: int
    available: bool

    def sell_item(self, amount):
        self.stock_amount -= amount

    def add_to_stock(self, amount):
        self.stock_amount += amount

    def is_available(self):
        return self.available

    def jsonify(self):
        return {**super().jsonify(),
                "price": self.price,
                "stock_amount": self.stock_amount,
                "available": self.available}
