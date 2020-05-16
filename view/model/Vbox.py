from PyQt5 import QtWidgets


class Vbox():
    def __init__(self, parent, name, items):
        self.vbox = QtWidgets.QVBoxLayout(parent)
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setObjectName(name)
        for i in range(len(items)):
            self.vbox.addWidget(items[i])
