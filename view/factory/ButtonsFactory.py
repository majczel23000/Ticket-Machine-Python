from view.model.Button import Button
from view.static.buttons_data import buttonsData


class ButtonsFactory:
    """
    Factory class for creating Button objects
    """

    def createTicketFirstZone(self, code):
        """
        Creating first zone tickets buttons
        :param code: first zone ticket code
        :return: Button class object
        """
        return Button(buttonsData['zone1'][code]['name'], buttonsData['zone1'][code]['text'], 0, 'TICKET_LABEL')

    def createTicketSecondZone(self, code):
        """
        Creating second zone tickets buttons
        :param code: second zone ticket code
        :return: Button class object
        """
        return Button(buttonsData['zone2'][code]['name'], buttonsData['zone2'][code]['text'], 0, 'TICKET_LABEL')

    def createMinusButton(self, name):
        """
        Creating button to reduce the quantity of specific ticket type
        :param name: name of button
        :return: Button class object
        """
        return Button(name, '-', 0, 'MINUS')

    def createPlusButton(self, name):
        """
        Creating button for increasing the quantity of specific ticket type
        :param name: name of button
        :return: Button class object
        """
        return Button(name, '+', 0, 'PLUS')

    def createCoinButton(self, code):
        """
        Creating button which look like Coin image
        :param code: code of button
        :return: Button class object with coin image background
        """
        return Button(buttonsData['coins'][code]['name'], "", buttonsData['coins'][code]['icon'])

    def createBanknoteButton(self, code):
        """
        Creating button which look like Banknote image
        :param code: code of button
        :return: Button class object with banknote image background
        """
        return Button(buttonsData['banknotes'][code]['name'], "", buttonsData['banknotes'][code]['icon'])