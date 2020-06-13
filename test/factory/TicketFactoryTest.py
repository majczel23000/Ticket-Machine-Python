import unittest

from src.factory.TicketFactory import TicketFactory
from src.model.Ticket import TicketNormalZone2, TicketReducedZone1, TicketReducedZone2, TicketNormalZone1


class TicketFactoryTest(unittest.TestCase):
    __ticketFactory = None

    @classmethod
    def setUp(cls):
        cls.__ticketFactory = TicketFactory()

    def test_ticket_normal_zone1(self):
        ticket = self.__ticketFactory.createTicket('normal', 1, 4.00, 'btn_normal_40_2')
        self.assertIsInstance(ticket, TicketNormalZone1)

    def test_ticket_reduced_zone1(self):
        ticket = self.__ticketFactory.createTicket('reduced', 1, 2.00, 'btn_normal_40_2')
        self.assertIsInstance(ticket, TicketReducedZone1)

    def test_ticket_normal_zone2(self):
        ticket = self.__ticketFactory.createTicket('normal', 2, 2.00, 'btn_normal_40')
        self.assertIsInstance(ticket, TicketNormalZone2)

    def test_ticket_reduced_zone2(self):
        ticket = self.__ticketFactory.createTicket('reduced', 2, 1.00, 'btn_normal_40')
        self.assertIsInstance(ticket, TicketReducedZone2)


if __name__ == '__main__':
    unittest.main()
