import sys
import unittest
from PyQt5 import QtWidgets
from src.model.TicketMachine import TicketMachine


class TicketMachineTest(unittest.TestCase):

    __ticketMachine = None

    @classmethod
    def setUp(cls):
        app = QtWidgets.QApplication(sys.argv)
        cls.__ticketMachine = TicketMachine()

    def test_singleton(self):
        app = QtWidgets.QApplication(sys.argv)
        instance = TicketMachine()
        self.assertTrue(instance == self.__ticketMachine)


if __name__ == '__main__':
    unittest.main()
