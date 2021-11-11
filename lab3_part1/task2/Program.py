# Pizzeria offers pizza-of-the-day for business lunch.
# The type of pizza-of-the-day depends on the day of week.
# Having a pizza-of-the-day simplifies ordering for customers.
# don't have to be experts on specific types of pizza.
# Also, customers can add extra ingredients to the pizza-of-the-day.
# Write a program that will form orders from customers.
from Menu import Menu
from Pizza import Pizza


def main():
    pizza1 = Pizza("Margeritha", 120, "Mozzarella", "Tomatoes", "Sauce")
    pizza2 = Pizza("Pepperoni", 130, "Mozzarella", "Pepperoni", "Sauce")
    menu = Menu({pizza1, pizza2}, (pizza1, pizza1, pizza1, pizza2, pizza2, pizza2, pizza2))


if __name__ == "__main__":
    main()
