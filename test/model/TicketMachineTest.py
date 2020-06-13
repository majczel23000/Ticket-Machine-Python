import sys
import unittest

from PyQt5 import QtWidgets

from src.model.TicketMachine import TicketMachine


class TicketMachineTest(unittest.TestCase):

    def test_singleton(self):
        app = QtWidgets.QApplication(sys.argv)
        instance1 = TicketMachine()
        instance2 = TicketMachine()
        self.assertTrue(instance1 == instance2)
