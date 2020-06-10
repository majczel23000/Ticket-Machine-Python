from abc import abstractmethod, ABCMeta


class IMoney(metaclass=ABCMeta):
    def __init__(self, value):
        self.value = value

    @staticmethod
    @abstractmethod
    def get_value():
        pass