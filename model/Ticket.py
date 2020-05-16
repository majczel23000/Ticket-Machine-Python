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
        print("Ticket first zone | price: ", self.price, " | type: ", self.type)


class TicketNormalZone1(ITicket):

    def get_info(self):
        print("Ticket first zone | price: ", self.price, " | type: ", self.type)


class TicketReducedZone2(ITicket):

    def get_info(self):
        print("Ticket first zone | price: ", self.price, " | type: ", self.type)


class TicketNormalZone2(ITicket):

    def get_info(self):
        print("Ticket first zone | price: ", self.price, " | type: ", self.type)
