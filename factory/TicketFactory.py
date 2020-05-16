from model.Ticket import TicketNormalZone1, TicketNormalZone2, TicketReducedZone1, TicketReducedZone2


class TicketFactory:

    @staticmethod
    def createTicket(ticket_type, zone_number, price, code):
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
