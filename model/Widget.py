from PyQt5 import QtWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self, parent, geometry, name):
        super(Widget, self).__init__()
        self.setParent(parent)
        self.setGeometry(geometry)
        self.setObjectName(name)