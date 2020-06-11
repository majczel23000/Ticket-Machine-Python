from PyQt5 import QtWidgets, QtGui


class Button(QtWidgets.QPushButton):
    """
    Button class of QPushButton type
    """

    def __init__(self, name, text, icon=0):
        """
        The constructor of button class which set up QPushButton object
        :param name: button name
        :param icon: icon object
        """
        super(Button, self).__init__()
        self.setObjectName(name)
        if text != 0:
            self.setText(text)
        if icon != 0:
            iconObj = QtGui.QIcon()
            iconObj.addPixmap(QtGui.QPixmap(icon['icon']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setMaximumSize(icon['iconSize'])
            self.setAutoFillBackground(False)
            self.setFlat(True)
            self.setIcon(iconObj)
            self.setIconSize(icon['iconSize'])
