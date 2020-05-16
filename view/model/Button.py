from PyQt5 import QtWidgets


class Button(QtWidgets.QPushButton):
    def __init__(self, name, text):
        super(Button, self).__init__()
        self.setObjectName(name)
        if text != 0:
            self.setText(text)