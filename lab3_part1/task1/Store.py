from datetime import date, datetime
import json
from Tickets import *


class Store:

    @staticmethod
    def get_data(title):
        if isinstance(title, str):
            with open(title.join(".json"), "r") as read_file:
                data = json.load(read_file)
        else:
            raise TypeError
        Store.__check_data(data)
        return data

    @staticmethod
    def __update_data(title):
        if not isinstance(title, str):
            raise TypeError
        new_data = Store.get_data(title)
        new_data["number_of_tickets"] -= 1
        with open(title.join(".json"), "w") as write_file:
            json.dump(new_data, write_file)

    @staticmethod
    def __check_title(title):
        if not isinstance(title, str):
            raise TypeError("Invalid title of event")
        if not title.strip():
            raise ValueError("Invalid title of event")

    @staticmethod
    def __check_price(price):
        if not isinstance(price, (float, int)):
            raise TypeError("Invalid price")
        if price <= 0.0:
            raise ValueError("Invalid price")

    @staticmethod
    def __check_date(start_date):
        if not isinstance(start_date, str):
            raise TypeError("Invalid date of event")
        date_of_event = datetime.strptime(start_date, '%Y.%M.%d')
        if (date_of_event - datetime.today()).days < 0:
            raise ValueError("Invalid date of event")

    @staticmethod
    def __check_quantity(quantity):
        if not isinstance(quantity, (float, int)):
            raise TypeError("Invalid quantity")
        if quantity < 0.0:
            raise ValueError("Invalid quantity")

    @staticmethod
    def __check_data(data):
        Store.__check_title(data["title"])
        Store.__check_price(data["ticket_price"])
        Store.__check_date(data["start_date"])
        Store.__check_quantity(data["number_of_tickets"])

    @staticmethod
    def buy_ticket(is_student=False):
        data = Store.get_data("event_info")
        if not data["number_of_tickets"]:
            return "There are no tickets"
        date_of_event = datetime.strptime(data["start_date"], '%Y.%M.%d')
        Store.__update_data("event_info")
        if(is_student):
            return StudentTicket(data["ticket_price"])
        dates_diffs = (date_of_event - datetime.today()).days
        if dates_diffs >= 60:
            return AdvanceTicket(data["ticket_price"])
        elif dates_diffs < 10:
            return LateTicket(data["ticket_price"])
        else:
            return RegularTicket(data["ticket_price"])

    @staticmethod
    def get_event_info():
        data = Store.get_data("event_info")
        title = data["title"]
        start_date = data["start_date"]
        price = data["ticket_price"]
        quantity = data["number_of_tickets"]
        return f"Event \"{title}\", which will start {start_date}. " \
               f"There are {quantity} tickets with regular price {price}$"
