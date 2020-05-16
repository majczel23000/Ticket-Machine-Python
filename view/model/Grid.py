from PyQt5 import QtWidgets


class Grid():
    def __init__(self, parent, name, items):
        self.grid = QtWidgets.QGridLayout(parent)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setObjectName(name)
        self.grid.addWidget(items[0], 1, 0, 1, 1)
        self.grid.addWidget(items[1], 2, 0, 1, 1)
        self.grid.addWidget(items[2], 3, 0, 1, 1)
        self.grid.addWidget(items[3], 4, 0, 1, 1)
