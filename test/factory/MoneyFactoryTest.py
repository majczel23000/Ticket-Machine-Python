import unittest

from src.factory.MoneyFactory import MoneyFactory
from src.model.Coin import Coin
from src.model.Banknote import Banknote


class MoneyFactoryTest(unittest.TestCase):
    __moneyFactory = None

    @classmethod
    def setUp(cls):
        cls.__moneyFactory = MoneyFactory()

    def test_coin(self):
        coin = self.__moneyFactory.createMoney('coin', 5.00)
        self.assertIsInstance(coin, Coin)

    def test_banknote(self):
        banknote = self.__moneyFactory.createMoney('banknote', 10.00)
        self.assertIsInstance(banknote, Banknote)

    def test_coin_value(self):
        value = 5.00
        coin = self.__moneyFactory.createMoney('coin', value)
        self.assertEqual(coin.get_value(), value)

    def test_banknote_value(self):
        value = 10.00
        banknote = self.__moneyFactory.createMoney('banknote', value)
        self.assertEqual(banknote.get_value(), value)


if __name__ == '__main__':
    unittest.main()
