from abc import abstractmethod, ABCMeta


class ITicket(metaclass=ABCMeta):
    def __init__(self, price, type, code):
        self.price = price
        self.type = type
        self.code = code

    @staticmethod
    @abstractmethod
    def get_info():
        pass


class TicketReducedZone1(ITicket):

    def get_info(self):
        return str("Ticket first zone | price: " + str(self.price) + " | type: " + str(self.type))


class TicketNormalZone1(ITicket):

    def get_info(self):
        return str("Ticket first zone | price: " + str(self.price) + " | type: " + str(self.type))


class TicketReducedZone2(ITicket):

    def get_info(self):
        return str("Ticket second zone | price: " + str(self.price) + " | type: " + str(self.type))


class TicketNormalZone2(ITicket):

    def get_info(self):
        return str("Ticket second zone | price: " + str(self.price) + " | type: " + str(self.type))
