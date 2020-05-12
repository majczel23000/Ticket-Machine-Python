from Banknote import Banknote
from Coin import Coin
from Ticket import Ticket


class Order:
    def __init__(self):
        self.storage = {
            '0.01': 0, '0.02': 0, '0.05': 0, '0.10': 0, '0.20': 0,
            '0.50': 0, '1.00': 0, '2.00': 0, '5.00': 0, '10.00': 0,
            '20.00': 0, '50.00': 0, '100.00': 0, '200.00': 0, '500.00': 0
        }
        self.tickets = list()
        self.cost = 0
        self.quantity = 0

    def add_ticket(self, ticket):
        if isinstance(ticket, Ticket):
            self.tickets.append(ticket)
            self.cost += ticket.price
            self.quantity += 1

    def insert_coin(self, coin):
        if isinstance(coin, Coin):
            self.storage[coin.value] += 1

    def insert_banknote(self, banknote):
        if isinstance(banknote, Banknote):
            self.storage[banknote.value] += 1
