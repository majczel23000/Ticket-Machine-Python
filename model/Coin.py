from model.IMoney import IMoney


class Coin(IMoney):
    """
    Coin class
    """

    def get_value(self):
        """
        Gets value of coin
        :return: value of coin
        """
        return self.value
