from Menu import Menu
from Schedule import Schedule
from datetime import datetime


class Order:

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.__total_value = 0
        self.__ordered = dict()

    @property
    def customer_name(self):
        return self.__customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        if not isinstance(customer_name, str):
            raise TypeError("Invalid type of name")
        self.__customer_name = customer_name

    def order_dish(self, title, quantity):
        dish = Menu.get_dish(title)
        if not dish:
            raise ValueError
        if dish["_Dish__name"] in self.__ordered.keys():
            self.__ordered[dish["_Dish__name"]]["quantity"] += quantity
        else:
            self.__ordered.update({dish["_Dish__name"]: {"dish": dish, "quantity": quantity}})
        self.__total_value += dish["_Dish__price"] * quantity

    def order_dish_of_the_day(self, quantity):
        dish = Schedule.get_dish(datetime.now().strftime("%A"))
        self.order_dish(dish['_Dish__name'], quantity)

    def del_from_order(self, title, quantity):
        dish = Menu.get_dish(title)
        if dish:
            if quantity < self.__ordered[dish["_Dish__name"]]["quantity"]:
                self.__ordered[dish["_Dish__name"]]["quantity"] -= quantity
            else:
                self.__ordered.pop(dish["_Dish__name"])
            self.__total_value -= dish["_Dish__price"] * quantity
        else:
            raise ValueError

    def add_extra_ingredient(self, ingredient, quantity):
        if not isinstance(ingredient, str):
            raise TypeError
        if ingredient in self.__ordered.keys():
            self.__ordered[ingredient]["quantity"] += quantity
        else:
            self.__ordered.update({ingredient: {"ingredient": ingredient, "quantity": quantity}})
        self.__total_value += 20 * quantity

    def __str__(self):
        return f"Customer: {self.customer_name}\n" \
               f"Order: {list(map(str, self.__ordered))}\n" \
               f"Total value: {self.__total_value}$"


