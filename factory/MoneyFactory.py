from model.Coin import Coin
from model.Banknote import Banknote


class MoneyFactory:

    @staticmethod
    def createMoney(money_type, value):
        if money_type == 'coin':
            return Coin(value)
        if money_type == 'banknote':
            return Banknote(value)
