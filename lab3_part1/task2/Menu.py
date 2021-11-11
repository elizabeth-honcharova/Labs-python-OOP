from Pizza import Pizza


class Menu:

    def __init__(self, types_of_pizza: set, schedule: tuple):
        self.types_of_pizza = types_of_pizza
        self.__schedule = dict(zip((0, 1, 2, 3, 4, 5, 6), schedule))

    @property
    def types_of_pizza(self):
        return self.__types_of_pizza

    @types_of_pizza.setter
    def types_of_pizza(self, types_of_pizza: set):
        if not isinstance(types_of_pizza, set) or not all(isinstance(pizza, Pizza) for pizza in types_of_pizza):
            raise TypeError("Invalid list of pizzas")
        self.__types_of_pizza = types_of_pizza

    @property
    def schedule(self):
        return self.__schedule

    @schedule.setter
    def schedule(self, schedule: tuple):
        if not isinstance(schedule, tuple) or not all(isinstance(pizza, Pizza) for pizza in schedule):
            raise TypeError("Invalid list of pizzas")
        if len(schedule) != 7:
            raise ValueError("Invalid list of pizzas")
        self.__schedule = dict(zip((0, 1, 2, 3, 4, 5, 6), schedule))

    def add_item_to_menu(self, pizza):
        if not isinstance(pizza, Pizza):
            raise TypeError("Invalid pizza")
        self.types_of_pizza.add(pizza)

    def change_schedule(self, dayweek: int, new_pizza: Pizza):
        if not isinstance(new_pizza, Pizza):
            raise TypeError("Invalid pizza")
        if not isinstance(dayweek, int):
            raise TypeError("Invalid day of week")
        if dayweek < 0 or dayweek >= 7:
            raise ValueError("Invalid day of week")
        self.schedule[dayweek] = new_pizza