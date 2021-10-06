class Product:

    def __init__(self, price=0.0, description='No description',
                 **dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (float, int)):
            raise TypeError("Invalid price")
        self.__price = price


class Customer:

    def __init__(self, surname='Unknown', name='Unknown',
                 patronymic='Unknown', phone=None):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    @property
    def full_name(self):
        return " ".join((str(self.surname), str(self.name), str(self.patronymic)))


class Order:

    id = 0

    def __init__(self, customer, *products):
        Order.id += 1
        if not isinstance(customer, Customer):
            raise TypeError("Invalid customer")
        for prod in products:
            if not isinstance(prod, Product):
                raise TypeError("Invalid product")
        self.customer = customer
        self.products = products

    def calc_total_val(self):
        total_value = 0.0
        for i in self.products:
            total_value += i.price
        return total_value

    def __str__(self):
        return "Order " + str(self.id) + '\nCustomer: ' + self.customer.full_name +\
            "\nTotal value: " + str(self.calc_total_val())


if __name__ == '__main__':

    shoes = Product(1200, "Sneakers Nike", size=37)
    hat = Product()

    Liza = Customer("Liza", "Honcharova", "Maksimovna", "+32423523425")
    Vova = Customer()

    order1 = Order(Liza, shoes, hat)
    print(order1)
    order2 = Order(Vova)
    print(order2)
