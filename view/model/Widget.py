from PyQt5 import QtWidgets


class Widget(QtWidgets.QWidget):
    """
    Widget class of QWidget type
    """

    def __init__(self, parent, geometry, name):
        """
        The constructor of widget class which set up QWidget object
        :param parent: widget parent
        :param geometry: geometry object
        :param name: widget name
        """
        super(Widget, self).__init__()
        self.setParent(parent)
        if geometry != 0:
            self.setGeometry(geometry)
        self.setObjectName(name)