# Write a program for selling tickets to IT-events. Each ticket has a unique number and a price.
# There are four types of tickets:
# regular ticket,
# advance ticket (purchased 60 or more days before the event),
# late ticket (purchased fewer than 10 days before the event)
# and student ticket.
# Additional information:
# -advance ticket - discount 40% of the regular ticket price;
# -student ticket - discount 50% of the regular ticket price;
# -late ticket - additional 10% to the regular ticket price.
# All tickets must have the following properties:
# -the ability to construct a ticket by number;
# -the ability to ask for a ticket’s price;
# -the ability to print a ticket as a String.

import json
from Store import Store
from Tickets import *


def create_event():
    event = {
        "title": "Int20h",
        "ticket_price": 600,
        "start_date": "2022.06.23",
        "number_of_tickets": 5000
        }
    return event


def serialize(data, title: str):
    if isinstance(title, str):
        with open(title.join(".json"), "w") as write_file:
            json.dump(data, write_file)
    else:
        raise TypeError


def main():
    serialize(create_event(), "event_info")
    store = Store()
    print(store.get_event_info())
    ticket1 = store.buy_ticket()
    print(ticket1, end='\n\n')
    print(store.get_event_info())
    ticket2 = store.buy_ticket(is_student=True)
    print(ticket2, end='\n\n')
    find_id = int(input("Enter the id of ticket you want to find: "))
    print(Ticket.find_ticket(find_id), end='\n\n')
    print("Price of the 1-st ticket: ", ticket1.price)


if __name__ == "__main__":
    main()
