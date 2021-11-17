class Dish:

    def __init__(self, name, price, *ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Invalid name")
        if not name.split():
            raise ValueError("Invalid name")
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (float, int)):
            raise TypeError("Invalid price")
        if price <= 0.0:
            raise ValueError("Invalid price")
        self.__price = price

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        if not all(isinstance(ingredient, str) for ingredient in ingredients):
            raise TypeError("Invalid ingredients")
        self.__ingredients = ingredients

    def __str__(self):
        return f"Dish \"{self.title}\": {self.price}$\n" \
               f"Ingredients: {list(map(str, self.__ingredients))}"
