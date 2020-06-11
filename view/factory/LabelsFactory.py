from view.model.Label import Label
from view.static.labels_data import labelsData

class LabelFactory:
    def createLabel(self, parent, code, font):
        return Label(parent, code, labelsData[code]['geometry'], font, labelsData[code]['alignment'], labelsData[code][
            'text'], labelsData[code]['style'])

    def createTicketLabel(self, code, text):
        return Label(0, code, 0, 0, 0, text, 0)
