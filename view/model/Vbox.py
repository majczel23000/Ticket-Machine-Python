from PyQt5 import QtWidgets


class Vbox():
    def __init__(self, parent, name, items):
        self.vbox = QtWidgets.QVBoxLayout(parent)
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setObjectName(name)
        self.vbox.addWidget(items[0])
        self.vbox.addWidget(items[1])
        self.vbox.addWidget(items[2])
        self.vbox.addWidget(items[3])
