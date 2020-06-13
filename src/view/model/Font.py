from PyQt5 import QtGui


class Font(QtGui.QFont):
    """
    Font class of QFont type
    """

    def __init__(self, family, size, bold, italic, weight):
        """
        The constructor of font class which set up QFont object
        :param family: font family type
        :param size: font size
        :param bold: determines if font will be bolded or not
        :param italic: determines if font will be italic or not
        :param weight: font weight
        """
        super(Font, self).__init__()
        self.setFamily(family)
        self.setPointSize(size)
        self.setBold(bold)
        self.setItalic(italic)
        self.setWeight(weight)