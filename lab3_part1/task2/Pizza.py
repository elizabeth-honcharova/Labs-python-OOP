import json
import os
from Dish import Dish


class Pizza(Dish):

    def __init__(self, name, price, *ingredients):
        super().__init__(name, price, *ingredients)

    def __str__(self):
        return f"Pizza \"{self.name}\": {self.price}$\n" \
               f"Ingredients: {list(map(str, self.__ingredients))}"
