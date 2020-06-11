from model.Ticket import TicketNormalZone1, TicketNormalZone2, TicketReducedZone1, TicketReducedZone2


class TicketFactory:
    """
    Factory class for creating tickets
    """

    @staticmethod
    def createTicket(ticket_type, zone_number, price, code):
        """
        Static method for creating tickets.
        :param ticket_type: ticket type to create
        :param zone_number: ticket zone number
        :param price: price of ticket to create
        :param code: code of ticket to create
        :return: specific ticket object
        """
        if ticket_type == 'normal':
            if zone_number == 1:
                return TicketNormalZone1(price, ticket_type, code)
            if zone_number == 2:
                return TicketNormalZone2(price, ticket_type, code)
        if ticket_type == 'reduced':
            if zone_number == 1:
                return TicketReducedZone1(price, ticket_type, code)
            if zone_number == 2:
                return TicketReducedZone2(price, ticket_type, code)
