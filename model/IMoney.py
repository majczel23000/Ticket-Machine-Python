from abc import abstractmethod, ABCMeta


class IMoney(metaclass=ABCMeta):
    """
    Base class of money
    """

    def __init__(self, value):
        """
        The constructor initializes the value field
        :param value: value of money
        """
        self.value = value

    @staticmethod
    @abstractmethod
    def get_value():
        """
        General value getting method
        :return: depends on implementation
        """
        pass