from PyQt5 import QtWidgets


class Label(QtWidgets.QLabel):
    def __init__(self, parent, name, geometry, font, alignment, text):
        super(Label, self).__init__()
        self.setParent(parent)
        self.setObjectName(name)
        if geometry != 0:
            self.setGeometry(geometry)
        if font != 0:
            self.setFont(font)
        if alignment != 0:
            self.setAlignment(alignment)
        if text != 0:
            self.setText(text)