from src.model.Coin import Coin
from src.model.Banknote import Banknote


class MoneyFactory:
    """
    Factory class for creating money
    """

    @staticmethod
    def createMoney(money_type, value):
        """
        Static method for creating money. Created money depends on money type.
        :param money_type: money type to create
        :param value: value of money to create
        :return: coin or banknote object
        """
        if money_type == 'coin':
            return Coin(value)
        if money_type == 'banknote':
            return Banknote(value)
