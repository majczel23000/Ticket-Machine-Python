from src.model.IMoney import IMoney


class Banknote(IMoney):
    """
    Banknote class
    """

    def get_value(self):
        """
        Gets value of banknote
        :return: value of banknote
        """
        return self.value
