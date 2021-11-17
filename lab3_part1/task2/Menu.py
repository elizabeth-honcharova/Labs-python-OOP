import json
import os
from Dish import Dish


class Menu:

    file_path = "menu.json"

    @staticmethod
    def add(dish):
        if not isinstance(dish, Dish):
            raise TypeError
        if os.path.isfile(Menu.file_path):
            if Menu.__check_unique(dish):
                data = Menu.__get_menu()
                data.append(dish.__dict__)
                with open(Menu.file_path, "w") as file:
                    json.dump(data, file)
        else:
            with open(Menu.file_path, "w") as file:
                data = [dish.__dict__]
                json.dump(data, file)

    @staticmethod
    def __check_unique(dish):
        for item in Menu.__get_menu():
            if item['_Dish__name'] == dish.name:
                return False
        return True

    @staticmethod
    def __get_menu():
        with open(Menu.file_path, "r") as menu:
            data = json.load(menu)
        return data

    @staticmethod
    def get_dish(title):
        if not isinstance(title, str):
            raise TypeError
        for item in Menu.__get_menu():
            if item['_Dish__name'] == title:
                return item
        return None

    @staticmethod
    def show():
        print("Menu: ")
        for line in Menu.__get_menu():
            print(line)
        print("\n")

