from PyQt5 import QtWidgets


class Grid(QtWidgets.QGridLayout):
    def __init__(self, parent, name, items):
        super(Grid, self).__init__()
        self.setParent(parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setObjectName(name)
        self.addWidget(items[0], 1, 0, 1, 1)
        self.addWidget(items[1], 2, 0, 1, 1)
        self.addWidget(items[2], 3, 0, 1, 1)
        self.addWidget(items[3], 4, 0, 1, 1)
