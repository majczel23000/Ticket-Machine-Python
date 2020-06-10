from view.model.Button import Button
from view.static.buttons_data import buttonsData


class ButtonsFactory:
    def createTicketFirstZone(self, code):
        return Button(buttonsData['zone1'][code]['name'], buttonsData['zone1'][code]['text'])

    def createTicketSecondZone(self, code):
        return Button(buttonsData['zone2'][code]['name'], buttonsData['zone2'][code]['text'])

    def createMinusButton(self, name):
        return Button(name, '-')

    def createPlusButton(self, name):
        return Button(name, '+')

    def createCoinButton(self, code):
        return Button(buttonsData['coins'][code]['name'], "", buttonsData['coins'][code]['icon'])

    def createBanknoteButton(self, code):
        return Button(buttonsData['banknotes'][code]['name'], "", buttonsData['banknotes'][code]['icon'])
