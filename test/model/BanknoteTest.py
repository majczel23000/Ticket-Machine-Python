import unittest
from src.model.Banknote import Banknote


class CoinTest(unittest.TestCase):
    __banknote = None

    @classmethod
    def setUp(cls):
        cls.__banknote = Banknote(10.00)

    def test_coin_instance(self):
        self.assertIsInstance(self.__banknote, Banknote)

    def test_coin_value(self):
        self.assertEqual(self.__banknote.get_value(), 10.00)
