from PyQt5 import QtCore, QtGui, QtWidgets
from src.view.factory.LabelsFactory import LabelFactory
from src.view.factory.WidgetFactory import WidgetFactory
from src.view.factory.FontFactory import FontFactory
from src.view.factory.ButtonsFactory import ButtonsFactory
from src.view.factory.GridFactory import GridFactory


class ConfirmationView(QtWidgets.QWidget):
    """
    Confirmation view class of QWidget type
    """

    def __init__(self):
        """
        The constructor of confirmation view class which set up: buttonsFactory, fontFactory, widgetFactory, gridFactory, labelFactory and setups UI
        :param parent: widget parent
        :param geometry: geometry object
        :param name: widget name
        """
        super(ConfirmationView, self).__init__()
        self.buttonsFactory = ButtonsFactory()
        self.fontFactory = FontFactory()
        self.widgetFactory = WidgetFactory()
        self.gridFactory = GridFactory()
        self.labelFactory = LabelFactory()
        self.setupUi()
        self.setupConfirmationView()

    def setupUi(self):
        """
        Set up main information about view
        """
        self.setObjectName("ConfirmationWidget")
        self.ConfirmationWidget = QtWidgets.QWidget(self)
        self.ConfirmationWidget.setObjectName("ConfirmationWidget")
        self.setAutoFillBackground(False)

    def setupConfirmationView(self):
        """
        Calls view generating methods
        """
        font = self.fontFactory.createFont('Consolas', 9, True, False, 75)
        self.setFont(font)
        self.generateMainLabels(font)
        self.generateLayouts()
        self.generateButtons()
        QtCore.QMetaObject.connectSlotsByName(self)

    def generateMainLabels(self, font):
        """
        Generates labels objects
        :param font: font object
        """
        font.setPointSize(18)
        self.label_title = self.labelFactory.createLabel(self.ConfirmationWidget, 'label_title', font)
        font.setPointSize(12)
        self.label_printing = self.labelFactory.createLabel(self.ConfirmationWidget, 'label_printing', font)
        self.label_your_tickets = self.labelFactory.createLabel(self.ConfirmationWidget, 'label_your_tickets', font)
        self.label_your_change = self.labelFactory.createLabel(self.ConfirmationWidget, 'label_your_change', font)
        self.label_thanks = self.labelFactory.createLabel(self.ConfirmationWidget, 'label_thanks', font)
        self.label_thanks.hide()

    def generateLayouts(self):
        """
        Generates layouts objects
        """
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.ConfirmationWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(490, 230, 431, 351))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.grid_your_change = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.grid_your_change.setContentsMargins(0, 0, 0, 0)
        self.grid_your_change.setObjectName("grid_your_change")
        self.vertical_confirmation = self.widgetFactory.createWidget(self.ConfirmationWidget, 'vertical_confirmation')

        self.layout_your_tickets = QtWidgets.QVBoxLayout(self.vertical_confirmation)
        self.layout_your_tickets.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout_your_tickets.setContentsMargins(0, 0, 0, 0)
        self.layout_your_tickets.setObjectName("layout_your_tickets")
        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.layout_your_tickets.addWidget(self.scroll)
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll.setWidget(self.scroll_widget)
        self.scroll_widget.setObjectName("scroll_your_tickets")

    def generateButtons(self):
        """
        Generates buttons objects
        """
        self.button_again = QtWidgets.QPushButton(self.ConfirmationWidget)
        self.button_again.setGeometry(QtCore.QRect(370, 652, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.button_again.setFont(font)
        self.button_again.setStyleSheet("border: 3px solid black; color: #f6f6f6; background: #3b3a30; font-size: 15px; ")
        self.button_again.setObjectName("button_again")
        self.button_again.setText("Ponowne zakupy")
        self.button_again.setDisabled(True)
