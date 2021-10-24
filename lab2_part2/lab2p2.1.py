import re


class Product:

    def __init__(self, price, description, **dimensions):
        self.price = price
        self.description = description
        self.__dimensions = dimensions

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
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("Invalid type of description")
        if not description:
            raise ValueError("Invalid description")
        self.__description = description

    def __str__(self):
        return f"{self.description}, {self.price}$: {self.__dimensions}"


class Customer:

    def __init__(self, surname, name, patronymic, phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Invalid type of surname")
        if not surname:
            raise ValueError("Invalid surname")
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Invalid type of name")
        if not name:
            raise ValueError("Invalid name")
        self.__name = name

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str):
            raise TypeError("Invalid type of patronymic")
        if not patronymic:
            raise ValueError("Invalid patronymic")
        self.__patronymic = patronymic

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Invalid type of phone")
        pattern = re.compile("^\\+?380[0-9]{9}")
        if not pattern.match(phone):
            raise ValueError("Invalid pattern of phone")
        self.__phone = phone

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}, {self.phone}"


class Order:

    def __init__(self, customer,  products):
        self.customer = customer
        self.products = products

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Invalid type of customer")
        self.__customer = customer

    @property
    def products(self):
        return list(map(str, self.__products))

    @products.setter
    def products(self, products):
        if not isinstance(products, dict):
            raise TypeError("Invalid type of products")
        if not all(isinstance(prod, Product) for prod in products.keys()):
            raise TypeError("Invalid type of product")
        if not all(num > 0 for num in products.values()):
            raise ValueError("Invalid number of product")
        self.__products = products

    @property
    def total_value(self):
        return self.__calc_total_value()

    def __calc_total_value(self):
        total_value = 0.0
        for prod in self.__products:
            total_value += prod.price * self.__products[prod]
        return total_value

    def add_product(self, product, number):
        if not isinstance(product, Product):
            raise TypeError("Invalid type of product")
        if number <= 0:
            raise ValueError("Invalid number of product")
        if product in self.__products.keys():
            self.__products[product] += number
        else:
            self.__products.update({product: number})

    def del_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Invalid type of product")
        if product in self.__products.keys():
            self.__products.pop(product)

    def __str__(self):
        return f"\n Customer: {self.customer}" \
               f"\n Products: {list(map(str, self.__products))}" \
               f"\n Total value: {self.total_value}$"


if __name__ == '__main__':

    shoes = Product(1200, "Sneakers Nike", size=37)
    shirt = Product(600, "Blue shirt", size="XS")

    Liza = Customer("Liza", "Honcharova", "Maksimovna", "+380683875855")
    Vova = Customer("Vova", "Bubka", "Batkovich", "380683875850")

    order1 = Order(Liza, {shoes: 2, shirt: 1})
    print(order1)

    order2 = Order(Vova, {})
    order2.add_product(shirt, 1)
    print(order2)
    order2.add_product(shirt, 1)
    print(order2)
    order2.del_product(shirt)
    print(order2)
