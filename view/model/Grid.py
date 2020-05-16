from PyQt5 import QtWidgets


class Grid():
    def __init__(self, parent, name, items):
        self.grid = QtWidgets.QGridLayout(parent)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setObjectName(name)
        for i in range(len(items)):
            self.grid.addWidget(items[i], i+1, 0, 1, 1)
