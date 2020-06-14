import unittest
from src.model.Coin import Coin


class CoinTest(unittest.TestCase):
    __coin = None

    @classmethod
    def setUp(cls):
        cls.__coin = Coin(5.00)

    def test_coin_instance(self):
        self.assertIsInstance(self.__coin, Coin)

    def test_coin_value(self):
        self.assertEqual(self.__coin.get_value(), 5.00)
