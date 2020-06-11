from view.model.Font import Font


class FontFactory:
    """
    Factory class for creating Font objects
    """

    def createFont(self, family, size, bold, italic, weight):
        """
        Creating Font object
        :param family: font family type
        :param size: font size
        :param bold: determines if the font must be bold or not
        :param italic: determines if the font must be italic or not
        :param weight: font weight
        :return: Font class object
        """
        return Font(family, size, bold, italic, weight)