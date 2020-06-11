from PyQt5 import QtWidgets


class Vbox():
    """
    Vbox class
    """

    def __init__(self, parent, name, items):
        """
        The constructor of vbox class which set up vbox
        :param parent: vbox parent
        :param name: vbox name
        :param items: list of items to insert into vbox
        """
        self.vbox = QtWidgets.QVBoxLayout(parent)
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setObjectName(name)
        for i in range(len(items)):
            self.vbox.addWidget(items[i])
