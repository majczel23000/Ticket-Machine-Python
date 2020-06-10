from PyQt5 import QtCore, QtGui, QtWidgets
from view.factory.WidgetFactory import WidgetFactory
from view.factory.ButtonsFactory import ButtonsFactory
from view.factory.FontFactory import FontFactory
from view.factory.LabelsFactory import LabelFactory


class PaymentView(QtWidgets.QWidget):
    def __init__(self):
        super(PaymentView, self).__init__()
        self.buttonsFactory = ButtonsFactory()
        self.fontFactory = FontFactory()
        self.widgetFactory = WidgetFactory()
        self.labelFactory = LabelFactory()
        self.setupUi()
        self.setupPaymentView()

    def setupPaymentView(self):
        font = self.fontFactory.createFont('Consolas', 9, True, False, 75)
        self.setFont(font)
        self.generateLabels(font)
        self.generateButtons()

    def generateLabels(self, font):
        font.setPointSize(18)
        self.label_title = self.labelFactory.createLabel(self.PaymentWidget, 'label_title', font)
        font.setPointSize(12)
        self.label_text = self.labelFactory.createLabel(self.PaymentWidget, 'label_text', font)
        self.horizontalLayoutWidget_2 = self.widgetFactory.createWidget(self.PaymentWidget, 'horizontal_payment_2')
        self.horizontal_payment = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontal_payment.setContentsMargins(0, 0, 0, 0)
        self.horizontal_payment.setSpacing(0)
        self.horizontal_payment.setObjectName("horizontal_payment")
        self.label_payment_left = self.labelFactory.createLabel(self.PaymentWidget, 'label_payment_left', font)
        self.horizontal_payment.addWidget(self.label_payment_left)
        self.label_payment_left_value = self.labelFactory.createLabel(self.PaymentWidget, 'label_payment_left_value', font)
        self.horizontal_payment.addWidget(self.label_payment_left_value)
        self.label_payment_change = self.labelFactory.createLabel(self.PaymentWidget, 'label_payment_change', font)
        self.horizontal_payment.addWidget(self.label_payment_change)
        self.label_payment_change_value = self.labelFactory.createLabel(self.PaymentWidget, 'label_payment_change_value', font)
        self.horizontal_payment.addWidget(self.label_payment_change_value)
        self.horizontalLayoutWidget = self.widgetFactory.createWidget(self.PaymentWidget, 'horizontal_payment')
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 540, 231, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontal_ticket_count = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontal_ticket_count.setContentsMargins(0, 0, 0, 0)
        self.horizontal_ticket_count.setSpacing(0)
        self.horizontal_ticket_count.setObjectName("horizontal_ticket_count")
        self.label_ticket_text = self.labelFactory.createLabel(self.PaymentWidget, 'label_ticket_text', font)
        self.horizontal_ticket_count.addWidget(self.label_ticket_text)
        self.label_ticket_count = self.labelFactory.createLabel(self.PaymentWidget, 'label_ticket_count', font)
        self.horizontal_ticket_count.addWidget(self.label_ticket_count)

    def generateButtons(self):
        self.gridLayoutWidget = QtWidgets.QWidget(self.PaymentWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 180, 341, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid_coins = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid_coins.setContentsMargins(0, 0, 0, 0)
        self.grid_coins.setObjectName("grid_coins")
        self.button_1_gr = self.buttonsFactory.createCoinButton("button_1_gr")
        self.button_2_gr = self.buttonsFactory.createCoinButton("button_2_gr")
        self.button_5_gr = self.buttonsFactory.createCoinButton("button_5_gr")
        self.button_10_gr = self.buttonsFactory.createCoinButton("button_10_gr")
        self.button_20_gr = self.buttonsFactory.createCoinButton("button_20_gr")
        self.button_50_gr = self.buttonsFactory.createCoinButton("button_50_gr")
        self.button_1_zl = self.buttonsFactory.createCoinButton("button_1_zl")
        self.button_2_zl = self.buttonsFactory.createCoinButton("button_2_zl")
        self.button_5_zl = self.buttonsFactory.createCoinButton("button_5_zl")
        self.grid_coins.addWidget(self.button_1_gr, 0, 0, 1, 1)
        self.grid_coins.addWidget(self.button_2_gr, 0, 1, 1, 1)
        self.grid_coins.addWidget(self.button_5_gr, 0, 2, 1, 1)
        self.grid_coins.addWidget(self.button_10_gr, 1, 0, 1, 1)
        self.grid_coins.addWidget(self.button_20_gr, 1, 1, 1, 1)
        self.grid_coins.addWidget(self.button_50_gr, 1, 2, 1, 1)
        self.grid_coins.addWidget(self.button_1_zl, 2, 0, 1, 1)
        self.grid_coins.addWidget(self.button_2_zl, 2, 1, 1, 1)
        self.grid_coins.addWidget(self.button_5_zl, 2, 2, 1, 1)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.PaymentWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(470, 180, 421, 401))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.grid_banknote = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.grid_banknote.setContentsMargins(0, 0, 0, 0)
        self.grid_banknote.setObjectName("grid_banknote")
        self.button_10_zl = self.buttonsFactory.createBanknoteButton("button_10_zl")
        self.button_20_zl = self.buttonsFactory.createBanknoteButton("button_20_zl")
        self.button_50_zl = self.buttonsFactory.createBanknoteButton("button_50_zl")
        self.button_100_zl = self.buttonsFactory.createBanknoteButton("button_100_zl")
        self.button_200_zl = self.buttonsFactory.createBanknoteButton("button_200_zl")
        self.button_500_zl = self.buttonsFactory.createBanknoteButton("button_500_zl")
        self.grid_banknote.addWidget(self.button_10_zl, 0, 0, 1, 1)
        self.grid_banknote.addWidget(self.button_20_zl, 0, 1, 1, 1)
        self.grid_banknote.addWidget(self.button_50_zl, 1, 0, 1, 1)
        self.grid_banknote.addWidget(self.button_100_zl, 1, 1, 1, 1)
        self.grid_banknote.addWidget(self.button_200_zl, 2, 0, 1, 1)
        self.grid_banknote.addWidget(self.button_500_zl, 2, 1, 1, 1)

    def setupUi(self):
        self.setObjectName("PaymentWidget")
        self.PaymentWidget = QtWidgets.QWidget(self)
        self.PaymentWidget.setObjectName("PaymentWidget")
        self.setAutoFillBackground(False)
        self.setStyleSheet("background:#ffeead")
        QtCore.QMetaObject.connectSlotsByName(self)



