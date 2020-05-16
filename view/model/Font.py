from PyQt5 import QtGui


class Font(QtGui.QFont):
    def __init__(self, family, size, bold, italic, weight):
        super(Font, self).__init__()
        self.setFamily(family)
        self.setPointSize(size)
        self.setBold(bold)
        self.setItalic(italic)
        self.setWeight(weight)