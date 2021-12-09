# Pizzeria offers pizza-of-the-day for business lunch.
# The type of pizza-of-the-day depends on the day of week.
# Having a pizza-of-the-day simplifies ordering for customers.
# don't have to be experts on specific types of pizza.
# Also, customers can add extra ingredients to the pizza-of-the-day.
# Write a program that will form orders from customers.
import os

from Menu import Menu
from Pizza import Pizza
from Schedule import Schedule
from Order import Order


def fill():
    pizza1 = Pizza("Margeritha", 120, "Mozzarella", "Tomatoes", "Sauce")
    pizza2 = Pizza("Pepperoni", 130, "Mozzarella", "Pepperoni", "Sauce")
    pizza3 = Pizza("Hawaiian", 110, "Chicken", "Pineapple", "Sauce")
    Menu.add(pizza1)
    Menu.add(pizza2)
    Menu.add(pizza3)
    Schedule.update_schedule("Monday", Menu.get_dish("Margeritha"))
    Schedule.update_schedule("Tuesday", Menu.get_dish("Margeritha"))
    Schedule.update_schedule("Wednesday", Menu.get_dish("Pepperoni"))
    Schedule.update_schedule("Thursday", Menu.get_dish("Pepperoni"))
    Schedule.update_schedule("Friday", Menu.get_dish("Hawaiian"))
    Schedule.update_schedule("Saturday", Menu.get_dish("Hawaiian"))
    Schedule.update_schedule("Sunday", Menu.get_dish("Hawaiian"))


def main():
    if os.path.isfile("menu.json"):
        os.remove("menu.json")
    fill()
    Menu.show()
    order = Order("Lizabeth")
    order.order_dish("Margeritha", 2)
    print("+2 Margeritha\n", order, end='\n\n')
    order.order_dish_of_the_day(1)
    print("+1 pizza of the day\n", order, end='\n\n')
    order.order_dish("Margeritha", 2)
    print("+2 Margeritha\n", order, end='\n\n')
    order.del_from_order("Margeritha", 4)
    print("-4 Margeritha\n", order, end='\n\n')
    order.add_extra_ingredient("Tomato", 2)
    print("+2 Tomato\n", order, end='\n\n')


if __name__ == "__main__":
    main()
