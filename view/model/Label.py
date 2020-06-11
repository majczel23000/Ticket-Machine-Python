from PyQt5 import QtWidgets


class Label(QtWidgets.QLabel):
    """
    Label class of QLabel type
    """

    def __init__(self, parent, name, geometry, font, alignment, text, style):
        """
        The constructor of label class which set up QLabel object
        :param parent: grid parent
        :param name: grid name
        :param geometry: geometry object
        :param font: font object
        :param alignment: alignment object
        :param text: label text
        :param style: label styles
        """
        super(Label, self).__init__()
        if parent != 0:
            self.setParent(parent)
        self.setObjectName(name)
        if geometry != 0:
            self.setGeometry(geometry)
        if font != 0:
            self.setFont(font)
        if alignment != 0:
            self.setAlignment(alignment)
        if text != 0:
            self.setText(text)
        if style != 0:
            self.setStyleSheet(style)
