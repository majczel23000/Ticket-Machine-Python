import unittest

from src.model.Coin import Coin
from src.model.Order import Order
from src.factory.TicketFactory import TicketFactory
from src.factory.MoneyFactory import MoneyFactory
from src.model.Ticket import TicketNormalZone2, TicketReducedZone2, TicketNormalZone1, TicketReducedZone1


class OrderTest(unittest.TestCase):

    __order = None

    @classmethod
    def setUp(cls):
        cls.__order = Order()
        cls.ticketFactory = TicketFactory()
        cls.moneyFactory = MoneyFactory()

    def test_tickets_count(self):
        self.helper_add_tickets()
        self.assertEqual(len(self.__order.get_tickets()), 4)

    def test_total_cost(self):
        total_cost = 9.00
        self.helper_add_tickets()
        self.assertEqual(self.__order.get_cost(), total_cost)

    def test_inserted_amount(self):
        money_inserted_value = 17.00
        self.helper_add_money()
        self.assertEqual(self.__order.get_inserted_amount(), money_inserted_value)

    def test_tickets_type(self):
        ticket = TicketNormalZone1(4.00, 'normal', 'btn_normal_40_2')
        self.__order.add_ticket(self.ticketFactory.createTicket('normal', 1, 4.00, 'btn_normal_40_2'))
        self.assertIsInstance(ticket, type(self.__order.get_tickets().pop()))

    def test_change_list(self):
        self.helper_add_tickets()
        self.helper_add_money()
        change_list = list()
        change_list.append(5.00)
        change_list.append(2.00)
        change_list.append(1.00)
        self.__order.calculate_exchange()
        self.assertEqual(change_list, self.__order.get_change_list())

    def test_clear_data(self):
        self.__order.set_cost(15)
        self.helper_add_tickets()
        self.helper_add_money()
        self.__order.clear_order_data()
        self.assertEqual(len(self.__order.get_tickets()), 0)
        self.assertEqual(len(self.__order.get_change_list()), 0)
        self.assertEqual(self.__order.get_inserted_amount(), 0)
        self.assertEqual(self.__order.get_cost(), 0)

    def helper_add_tickets(self):
        self.__order.add_ticket(self.ticketFactory.createTicket('normal', 1, 4.00, 'btn_normal_40_2'))
        self.__order.add_ticket(self.ticketFactory.createTicket('reduced', 1, 2.00, 'btn_reduced_40_2'))
        self.__order.add_ticket(self.ticketFactory.createTicket('normal', 2, 2.00, 'btn_normal_40'))
        self.__order.add_ticket(self.ticketFactory.createTicket('reduced', 2, 1.00, 'btn_reduced_40'))

    def helper_add_money(self):
        self.__order.insert_money(self.moneyFactory.createMoney('coin', 2.00))
        self.__order.insert_money(self.moneyFactory.createMoney('coin', 5.00))
        self.__order.insert_money(self.moneyFactory.createMoney('banknote', 10.00))
