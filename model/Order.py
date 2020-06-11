import math

from model.Banknote import Banknote
from model.Coin import Coin
from model.Ticket import TicketReducedZone1, TicketReducedZone2, TicketNormalZone1, TicketNormalZone2
from decimal import Decimal


class Order:
    def __init__(self):
        self.money_inserted = list()
        self.tickets = list()
        self.change_list = list()
        self.cost = 0
        self.quantity = 0
        self.money_inserted_value = 0

    def add_ticket(self, ticket):
        if isinstance(ticket, TicketReducedZone1) or isinstance(ticket, TicketReducedZone2) \
                or isinstance(ticket, TicketNormalZone1) or isinstance(ticket, TicketNormalZone2):
            self.tickets.append(ticket)
            self.cost += float(ticket.price)
            self.cost = float(round(Decimal(self.cost), 2))
            self.quantity += 1

    def insert_money(self, money):
        if isinstance(money, Coin) or isinstance(money, Banknote):
            self.money_inserted.append(money)
            self.count_amount()

    def count_amount(self):
        self.money_inserted_value = 0
        for m in self.money_inserted:
            self.money_inserted_value += float(m.value)
        self.money_inserted_value = float(round(Decimal(self.money_inserted_value), 2))

    def calculate_exchange(self):
        if self.money_inserted_value == self.cost:
            print("no exchange")
            return
        exchange = self.money_inserted_value - self.cost
        i = 0
        values = [500.00, 200.00, 100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
        while exchange > 0 and i <= len(values):
            if exchange >= values[i]:
                P = math.floor(exchange/values[i])
                exchange = round(100*(exchange-(values[i]*P)))/100
                for x in range(0,P):
                    self.change_list.append(values[i])
            i += 1

    def get_inserted_amount(self):
        return self.money_inserted_value

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost

    def get_tickets(self):
        return self.tickets

    def get_change_list(self):
        return self.change_list
