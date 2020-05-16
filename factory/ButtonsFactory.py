from model.Button import Button
from common.buttons_data import buttonsData


class ButtonsFactory:
    def createTicketFirstZone(self, code):
        return Button(buttonsData['zone1'][code]['name'], buttonsData['zone1'][code]['text'])

    def createTicketSecondZone(self, code):
        return Button(buttonsData['zone2'][code]['name'], buttonsData['zone1'][code]['text'])

    def createMinusButton(self, name):
        return Button(name, '-')

    def createPlusButton(self, name):
        return Button(name, '+')
