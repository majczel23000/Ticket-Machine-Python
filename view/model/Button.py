from PyQt5 import QtWidgets, QtGui


class Button(QtWidgets.QPushButton):
    def __init__(self, name, text, icon=0):
        super(Button, self).__init__()
        self.setObjectName(name)
        if text != 0:
            self.setText(text)
        if icon != 0:
            print(icon['icon'])
            iconObj = QtGui.QIcon()
            iconObj.addPixmap(QtGui.QPixmap(icon['icon']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setMaximumSize(icon['iconSize'])
            self.setAutoFillBackground(False)
            self.setFlat(True)
            self.setIcon(iconObj)
            self.setIconSize(icon['iconSize'])
