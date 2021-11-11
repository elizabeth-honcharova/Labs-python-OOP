from Menu import Menu
from Pizza import Pizza

class Order:

    def __init__(self):
        self.total_value = 0
        self.ordered = dict()

    def order_pizza(self, pizza, quantity_with_diameter: dict):
        pass

    def order_pizza_of_the_day(self, quantity_with_diameter: dict):
        pass

    def del_from_order(self):
        pass

    def add_ingredients(self, *ingredients):
        pass

    def __str__(self):
        pass