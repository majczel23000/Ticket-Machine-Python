from src.view.model.Label import Label
from src.view.static.labels_data import labelsData

class LabelFactory:
    """
    Factory class for creating Labels objects
    """

    def createLabel(self, parent, code, font):
        """
        Creating Label object
        :param parent: parent where label will be inserted
        :param code: label code
        :param font: Font object
        :return: Label class object
        """
        return Label(parent, code, labelsData[code]['geometry'], font, labelsData[code]['alignment'], labelsData[code][
            'text'], labelsData[code]['style'])

    def createTicketLabel(self, code, text):
        """
        Creating Label object
        :param code: label code
        :param text: label text
        :return: Label class object
        """
        return Label(0, code, 0, 0, 0, text, 0)
