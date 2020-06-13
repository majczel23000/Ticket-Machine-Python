from PyQt5 import QtWidgets, QtGui


class Button(QtWidgets.QPushButton):
    """
    Button class of QPushButton type
    """

    def __init__(self, name, text, icon, destination=0):
        """
        The constructor of button class which set up QPushButton object
        :param name: button name
        :param icon: icon object
        :param destination: where button will be used (as what)
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
        if destination == "MINUS":
            self.setStyleSheet('height: 50px; font-size: 15px;background: #FF5948; color: black; border: 5px solid black; padding: 10px')
        elif destination == "PLUS":
            self.setStyleSheet('font-weight: bold; font-size: 50px; height: 50px; font-size: 15px;background: #5BC900; color: black; border: 5px solid black; padding: 10px')
        elif destination == "TICKET_LABEL":
            self.setStyleSheet('font-weight: bold; height: 50px; font-size: 13px; text-transform: uppercase; background: #0074BF; color: black; border: 5px solid black; padding: 10px')