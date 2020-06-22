import math

from src.model.Banknote import Banknote
from src.model.Coin import Coin
from src.model.Ticket import TicketReducedZone1, TicketReducedZone2, TicketNormalZone1, TicketNormalZone2
from decimal import Decimal


class Order:
    """
    Order class
    """

    def __init__(self):
        """
        The constructor of order class which initializes the field: money_inserted, tickets, change_list, cost,
        quantity, money_inserted_value
        """
        self.money_inserted = list()
        self.tickets = list()
        self.change_list = list()
        self.cost = 0
        self.quantity = 0
        self.money_inserted_value = 0

    def add_ticket(self, ticket):
        """
        Checking ticket to add type and adding it to selected ticket list
        :param ticket: ticket object to add
        """
        if isinstance(ticket, TicketReducedZone1) or isinstance(ticket, TicketReducedZone2) \
                or isinstance(ticket, TicketNormalZone1) or isinstance(ticket, TicketNormalZone2):
            self.tickets.append(ticket)
            self.cost += float(ticket.price)
            self.cost = float(round(Decimal(self.cost), 2))
            self.quantity += 1

    def insert_money(self, money):
        """
        Checking money to insert type and adding it to inserted money list
        :param money: money object (Coin or Banknote) to add
        """
        if isinstance(money, Coin) or isinstance(money, Banknote):
            self.money_inserted.append(money)
            self.count_amount()

    def count_amount(self):
        """
        Calculates total value of inserted money
        """
        self.money_inserted_value = 0
        for m in self.money_inserted:
            self.money_inserted_value += float(m.value)
        self.money_inserted_value = float(round(Decimal(self.money_inserted_value), 2))

    def calculate_exchange(self):
        """
        Calculates change for order
        """
        if self.money_inserted_value == self.cost:
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

    def clear_order_data(self):
        """
        Reset all order data
        """
        self.money_inserted_value = 0
        self.cost = 0
        self.tickets = list()
        self.quantity = 0
        self.change_list = list()
        self.money_inserted = list()

    def get_inserted_amount(self):
        """
        Get total value of inserted money
        :return: total value of inserted money
        """
        return self.money_inserted_value

    def get_cost(self):
        """
        Get total cost of selected tickets
        :return: total cost of selected tickets
        """
        return self.cost

    def set_cost(self, cost):
        """
        Set total cost of selected tickets
        :param cost: total cost of selected tickets
        """
        self.cost = cost

    def get_tickets(self):
        """
        Get selected tickets list
        :return: selected tickets list
        """
        return self.tickets

    def get_change_list(self):
        """
        Get list of change money
        :return: list of change money
        """
        return self.change_list
