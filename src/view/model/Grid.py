from PyQt5 import QtWidgets


class Grid():
    """
    Grid class
    """

    def __init__(self, parent, name, items):
        """
        The constructor of grid class which set up grid
        :param parent: grid parent
        :param name: grid name
        :param items: list of items to insert into grid
        """
        self.grid = QtWidgets.QGridLayout(parent)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setObjectName(name)
        for i in range(len(items)):
            self.grid.addWidget(items[i], i+1, 0, 1, 1)
