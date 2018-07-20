""" Robbie's first question, what does mypy output with this code?"""
class Item:
    def __init__(self, price: float):
        self.price = price

item = Item(price=1.5)
item.price + "abc"
