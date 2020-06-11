from abc import abstractmethod, ABCMeta


class ITicket(metaclass=ABCMeta):
    """
    Base class of tickets
    """

    def __init__(self, price, type, code):
        """
        The constructor initializes the fields: price, code and type
        :param price: price of ticket
        :param type: ticket type
        :param code: ticket code
        """
        self.price = price
        self.type = type
        self.code = code

    @staticmethod
    @abstractmethod
    def get_info():
        """
        General information getting method
        :return: depends on implementation
        """
        pass


class TicketReducedZone1(ITicket):
    """
    Reduced ticket zone 1 class
    """

    def get_info(self):
        """
        Return reduced ticket zone 1 description
        :return: string information about ticket
        """
        return str("Ticket first zone | price: " + str(self.price) + " | type: " + str(self.type))


class TicketNormalZone1(ITicket):
    """
    Normal ticket zone 1 class
    """

    def get_info(self):
        """
        Return normal ticket zone 1 description
        :return: string information about ticket
        """
        return str("Ticket first zone | price: " + str(self.price) + " | type: " + str(self.type))


class TicketReducedZone2(ITicket):
    """
    Reduced ticket zone 2 class
    """

    def get_info(self):
        """
        Return reduced ticket zone 2 description
        :return: string information about ticket
        """
        return str("Ticket second zone | price: " + str(self.price) + " | type: " + str(self.type))


class TicketNormalZone2(ITicket):
    """
    Normal ticket zone 2 class
    """

    def get_info(self):
        """
        Return normal ticket zone 1 description
        :return: string information about ticket
        """
        return str("Ticket second zone | price: " + str(self.price) + " | type: " + str(self.type))
