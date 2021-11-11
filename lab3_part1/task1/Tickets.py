class Ticket:

    counter = 0
    tickets = {}

    def __init__(self, price, price_scale):
        self.price = price * price_scale
        Ticket.counter += 1
        self.id = Ticket.counter
        Ticket.tickets.update({self.id: self.price})

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

    @staticmethod
    def find_ticket(id):
        if id in Ticket.tickets.keys():
            return f"Ticket №: {id} | price: {Ticket.tickets[id]}$"
        else:
            return "No tickets found"

    def __str__(self):
        return f"Ticket №: {self.id} | price: {self.price}$"


class RegularTicket(Ticket):

    def __init__(self, price):
        super().__init__(price, 1)

    def __str__(self):
        return f"Ticket №: {self.id} | regular price: {self.price}$"


class AdvanceTicket(Ticket):

    def __init__(self, price):
        super().__init__(price, 0.6)

    def __str__(self):
        return f"Ticket №: {self.id} | advance price: {self.price}$"


class LateTicket(Ticket):

    def __init__(self, price):
        super().__init__(price, 1.1)

    def __str__(self):
        return f"Ticket №: {self.id} | late price: {self.price}$"


class StudentTicket(Ticket):

    def __init__(self, price):
        super().__init__(price, 0.5)

    def __str__(self):
        return f"Ticket №: {self.id} | student price: {self.price}$"
