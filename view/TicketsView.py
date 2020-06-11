from PyQt5 import QtCore, QtWidgets
from view.factory.WidgetFactory import WidgetFactory
from view.factory.ButtonsFactory import ButtonsFactory
from view.factory.FontFactory import FontFactory
from view.factory.GridFactory import GridFactory
from view.factory.LabelsFactory import LabelFactory
from view.factory.VboxFactory import VboxFactory


class TicketsView(QtWidgets.QWidget):
    def __init__(self):
        super(TicketsView, self).__init__()
        self.buttonsFactory = ButtonsFactory()
        self.fontFactory = FontFactory()
        self.widgetFactory = WidgetFactory()
        self.gridFactory = GridFactory()
        self.labelFactory = LabelFactory()
        self.vboxFactory = VboxFactory()
        self.setupUi()
        self.setupTicketsView()


    # pokazanie widoku wybierania biletów
    def setupTicketsView(self):
        font = self.fontFactory.createFont('Consolas', 9, True, False, 75)
        self.setFont(font)
        self.generateMainLabels(font)
        self.generateBottomView(font)
        # self.setCentralWidget(self.TicketsWidget)
        self.generateButtonsAndLabelsPlusMinus(font)
        self.generateButtonsTicketsWithNames()
        self.generateCosmetics()
        QtCore.QMetaObject.connectSlotsByName(self)

    def setupUi(self):
        self.setObjectName("TicketsWidget")
        self.TicketsWidget = QtWidgets.QWidget(self)
        self.TicketsWidget.setObjectName("TicketsWidget")

    def generateMainLabels(self, font):
        font.setPointSize(18)
        self.label_title = self.labelFactory.createLabel(self.TicketsWidget, 'label_title', font)
        font.setPointSize(14)
        self.label_tickets_reduced = self.labelFactory.createLabel(self.TicketsWidget, 'label_tickets_reduced', font)
        self.label_tickets_normal = self.labelFactory.createLabel(self.TicketsWidget, 'label_tickets_normal', font)
        font.setPointSize(13)
        self.label_strefa_1 = self.labelFactory.createLabel(self.TicketsWidget, 'label_strefa_1', font)
        self.label_strefa_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_strefa_1.setTextFormat(QtCore.Qt.PlainText)
        self.label_strefa_1.setWordWrap(True)
        self.label_strefa_2 = self.labelFactory.createLabel(self.TicketsWidget, 'label_strefa_2', font)
        self.label_strefa_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_strefa_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_strefa_2.setWordWrap(True)

    def generateBottomView(self, font):
        self.horizontalLayoutWidget = self.widgetFactory.createWidget(self.TicketsWidget, 'horizontalLayoutWidget')
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_total_cost = self.labelFactory.createLabel(self.horizontalLayoutWidget, 'label_total_cost', 0)
        self.label_total_cost_value = self.labelFactory.createLabel(self.horizontalLayoutWidget, 'label_total_cost_value', 0)
        self.label_tickets_count = self.labelFactory.createLabel(self.horizontalLayoutWidget, 'label_tickets_count', 0)
        self.label_tickets_count_value = self.labelFactory.createLabel(self.horizontalLayoutWidget, 'label_tickets_count_value', 0)
        self.horizontalLayout.addWidget(self.label_total_cost)
        self.horizontalLayout.addWidget(self.label_total_cost_value)
        self.horizontalLayout.addWidget(self.label_tickets_count)
        self.horizontalLayout.addWidget(self.label_tickets_count_value)
        self.payment = QtWidgets.QPushButton(self.TicketsWidget)
        self.payment.setGeometry(QtCore.QRect(610, 660, 331, 61))
        font.setPointSize(15)
        self.payment.setFont(font)
        self.payment.setObjectName("payment")
        self.payment.setText('Przejdź do płatności')

    def generateButtonsAndLabelsPlusMinus(self, font):
        self.verticalLayoutWidget = self.widgetFactory.createWidget(self.TicketsWidget, 'verticalLayoutWidget')
        self.btn_reduced_20_2_minus = self.buttonsFactory.createMinusButton('btn_reduced_20_2_minus')
        self.btn_reduced_40_2_minus = self.buttonsFactory.createMinusButton('btn_reduced_40_2_minus')
        self.btn_reduced_oneway_2_minus = self.buttonsFactory.createMinusButton('btn_reduced_oneway_2_minus')
        self.btn_reduced_twoway_2_minus = self.buttonsFactory.createMinusButton('btn_reduced_twoway_2_minus')
        self.layout_reduced_second_minus = self.vboxFactory.createVbox(self.verticalLayoutWidget, 'layout_reduced_second_minus', [
            self.btn_reduced_20_2_minus, self.btn_reduced_40_2_minus, self.btn_reduced_oneway_2_minus, self.btn_reduced_twoway_2_minus
        ])

        self.verticalLayoutWidget_2 = self.widgetFactory.createWidget(self.TicketsWidget, 'verticalLayoutWidget_2')
        self.btn_reduced_20_2_plus = self.buttonsFactory.createPlusButton('btn_reduced_20_2_plus')
        self.btn_reduced_40_2_plus = self.buttonsFactory.createPlusButton('btn_reduced_40_2_plus')
        self.btn_reduced_oneway_2_plus = self.buttonsFactory.createPlusButton('btn_reduced_oneway_2_plus')
        self.btn_reduced_twoway_2_plus = self.buttonsFactory.createPlusButton('btn_reduced_twoway_2_plus')
        self.layout_reduced_second_plus = self.vboxFactory.createVbox(self.verticalLayoutWidget_2, 'layout_reduced_second_plus', [
            self.btn_reduced_20_2_plus, self.btn_reduced_40_2_plus, self.btn_reduced_oneway_2_plus, self.btn_reduced_twoway_2_plus
        ])

        font.setPointSize(12)
        self.verticalLayoutWidget_3 = self.widgetFactory.createWidget(self.TicketsWidget, 'verticalLayoutWidget_3')
        self.btn_reduced_20_2_count = self.labelFactory.createLabel(self.verticalLayoutWidget_3, 'btn_reduced_20_2_count', font)
        self.btn_reduced_40_2_count = self.labelFactory.createLabel(self.verticalLayoutWidget_3, 'btn_reduced_40_2_count', font)
        self.btn_reduced_oneway_2_count = self.labelFactory.createLabel(self.verticalLayoutWidget_3, 'btn_reduced_oneway_2_count', font)
        self.btn_reduced_twoway_2_count = self.labelFactory.createLabel(self.verticalLayoutWidget_3, 'btn_reduced_twoway_2_count', font)
        self.layout_reduced_second_count = self.vboxFactory.createVbox(self.verticalLayoutWidget_3, 'layout_reduced_second_count', [
            self.btn_reduced_20_2_count, self.btn_reduced_40_2_count, self.btn_reduced_oneway_2_count, self.btn_reduced_twoway_2_count
        ])

        self.verticalLayoutWidget_4 = self.widgetFactory.createWidget(self.TicketsWidget, 'verticalLayoutWidget_4')
        self.btn_reduced_20_minus = self.buttonsFactory.createMinusButton('btn_reduced_20_minus')
        self.btn_reduced_40_minus = self.buttonsFactory.createMinusButton('btn_reduced_40_minus')
        self.btn_reduced_oneway_minus = self.buttonsFactory.createMinusButton('btn_reduced_oneway_minus')
        self.btn_reduced_twoway_minus = self.buttonsFactory.createMinusButton('btn_reduced_twoway_minus')
        self.verticalLayout_7 = self.vboxFactory.createVbox(self.verticalLayoutWidget_4, 'verticalLayout_7', [
            self.btn_reduced_20_minus, self.btn_reduced_40_minus, self.btn_reduced_oneway_minus, self.btn_reduced_twoway_minus
        ])

        self.verticalLayoutWidget_5 = self.widgetFactory.createWidget(self.TicketsWidget, 'verticalLayoutWidget_5')
        self.btn_normal_20_minus = self.buttonsFactory.createMinusButton('btn_normal_20_minus')
        self.btn_normal_40_minus = self.buttonsFactory.createMinusButton('btn_normal_40_minus')
        self.btn_normal_oneway_minus = self.buttonsFactory.createMinusButton('btn_normal_oneway_minus')
        self.btn_normal_twoway_minus = self.buttonsFactory.createMinusButton('btn_normal_twoway_minus')
        self.layout_normal_first_minus = self.vboxFactory.createVbox(self.verticalLayoutWidget_5, 'layout_normal_first_minus', [
            self.btn_normal_20_minus, self.btn_normal_40_minus, self.btn_normal_oneway_minus, self.btn_normal_twoway_minus
        ])

        self.verticalLayoutWidget_6 = self.widgetFactory.createWidget(self.TicketsWidget, 'verticalLayoutWidget_6')
        self.btn_normal_20_2_minus = self.buttonsFactory.createMinusButton('btn_normal_20_2_minus')
        self.btn_normal_40_2_minus = self.buttonsFactory.createMinusButton('btn_normal_40_2_minus')
        self.btn_normal_oneway_2_minus = self.buttonsFactory.createMinusButton('btn_normal_oneway_2_minus')
        self.btn_normal_twoway_2_minus = self.buttonsFactory.createMinusButton('btn_normal_twoway_2_minus')
        self.layout_normal_second_minus = self.vboxFactory.createVbox(self.verticalLayoutWidget_6, 'layout_normal_second_minus', [
            self.btn_normal_20_2_minus, self.btn_normal_40_2_minus, self.btn_normal_oneway_2_minus, self.btn_normal_twoway_2_minus
        ])

        self.verticalLayoutWidget_7 = self.widgetFactory.createWidget(self.TicketsWidget, 'verticalLayoutWidget_7')
        self.btn_normal_20_count = self.labelFactory.createLabel(self.verticalLayoutWidget_3, 'btn_normal_20_count', font)
        self.btn_normal_40_count = self.labelFactory.createLabel(self.verticalLayoutWidget_3, 'btn_normal_40_count', font)
        self.btn_normal_oneway_count = self.labelFactory.createLabel(self.verticalLayoutWidget_3, 'btn_normal_oneway_count', font)
        self.btn_normal_twoway_count = self.labelFactory.createLabel(self.verticalLayoutWidget_3, 'btn_normal_twoway_count', font)
        self.layout_normal_first_count = self.vboxFactory.createVbox(self.verticalLayoutWidget_7, 'layout_normal_first_count', [
            self.btn_normal_20_count, self.btn_normal_40_count, self.btn_normal_oneway_count, self.btn_normal_twoway_count
        ])

        self.verticalLayoutWidget_8 = self.widgetFactory.createWidget(self.TicketsWidget, 'verticalLayoutWidget_8')
        self.btn_normal_20_2_count = self.labelFactory.createLabel(self.verticalLayoutWidget_3, 'btn_normal_20_2_count', font)
        self.btn_normal_40_2_count = self.labelFactory.createLabel(self.verticalLayoutWidget_3, 'btn_normal_40_2_count', font)
        self.btn_normal_oneway_2_count = self.labelFactory.createLabel(self.verticalLayoutWidget_3, 'btn_normal_oneway_2_count', font)
        self.btn_normal_twoway_2_count = self.labelFactory.createLabel(self.verticalLayoutWidget_3, 'btn_normal_twoway_2_count', font)
        self.layout_normal_second_count = self.vboxFactory.createVbox(self.verticalLayoutWidget_8, 'layout_normal_second_count', [
            self.btn_normal_20_2_count, self.btn_normal_40_2_count, self.btn_normal_oneway_2_count, self.btn_normal_twoway_2_count
        ])

        self.verticalLayoutWidget_9 = self.widgetFactory.createWidget(self.TicketsWidget, 'verticalLayoutWidget_9')
        self.btn_normal_20_plus = self.buttonsFactory.createPlusButton('btn_normal_20_plus')
        self.btn_normal_40_plus = self.buttonsFactory.createPlusButton('btn_normal_40_plus')
        self.btn_normal_oneway_plus = self.buttonsFactory.createPlusButton('btn_normal_oneway_plus')
        self.btn_normal_twoway_plus = self.buttonsFactory.createPlusButton('btn_normal_twoway_plus')
        self.layout_normal_first_plus = self.vboxFactory.createVbox(self.verticalLayoutWidget_9, 'layout_normal_first_plus', [
            self.btn_normal_20_plus, self.btn_normal_40_plus, self.btn_normal_oneway_plus, self.btn_normal_twoway_plus
        ])

        self.verticalLayoutWidget_10 = self.widgetFactory.createWidget(self.TicketsWidget, 'verticalLayoutWidget_10')
        self.btn_normal_20_2_plus = self.buttonsFactory.createPlusButton('btn_normal_20_2_plus')
        self.btn_normal_40_2_plus = self.buttonsFactory.createPlusButton('btn_normal_40_2_plus')
        self.btn_normal_oneway_2_plus = self.buttonsFactory.createPlusButton('btn_normal_oneway_2_plus')
        self.btn_normal_twoway_2_plus = self.buttonsFactory.createPlusButton('btn_normal_twoway_2_plus')
        self.layout_normal_second_plus = self.vboxFactory.createVbox(self.verticalLayoutWidget_10, 'layout_normal_second_plus', [
            self.btn_normal_20_2_plus, self.btn_normal_40_2_plus, self.btn_normal_oneway_2_plus, self.btn_normal_twoway_2_plus
        ])

        self.verticalLayoutWidget_11 = self.widgetFactory.createWidget(self.TicketsWidget, 'verticalLayoutWidget_11')
        self.btn_reduced_20_count = self.labelFactory.createLabel(self.verticalLayoutWidget_3, 'btn_reduced_20_count', font)
        self.btn_reduced_40_count = self.labelFactory.createLabel(self.verticalLayoutWidget_3, 'btn_reduced_40_count', font)
        self.btn_reduced_oneway_count = self.labelFactory.createLabel(self.verticalLayoutWidget_3, 'btn_reduced_oneway_count', font)
        self.btn_reduced_twoway_count = self.labelFactory.createLabel(self.verticalLayoutWidget_3, 'btn_reduced_twoway_count', font)
        self.layout_reduced_first_count = self.vboxFactory.createVbox(self.verticalLayoutWidget_11, 'layout_reduced_first_count', [
            self.btn_reduced_20_count, self.btn_reduced_40_count, self.btn_reduced_oneway_count, self.btn_reduced_twoway_count
        ])

        self.verticalLayoutWidget_12 = self.widgetFactory.createWidget(self.TicketsWidget, 'verticalLayoutWidget_12')
        self.btn_reduced_20_plus = self.buttonsFactory.createPlusButton('btn_reduced_20_plus')
        self.btn_reduced_40_plus = self.buttonsFactory.createPlusButton('btn_reduced_40_plus')
        self.btn_reduced_oneway_plus = self.buttonsFactory.createPlusButton('btn_reduced_oneway_plus')
        self.btn_reduced_twoway_plus = self.buttonsFactory.createPlusButton('btn_reduced_twoway_plus')
        self.layout_reduced_first_plus = self.vboxFactory.createVbox(self.verticalLayoutWidget_12, 'layout_reduced_first_plus', [
            self.btn_reduced_20_plus, self.btn_reduced_40_plus, self.btn_reduced_oneway_plus, self.btn_reduced_twoway_plus
        ])

    def generateButtonsTicketsWithNames(self):
        # REDUCED ZONE 1
        self.btn_reduced_20 = self.buttonsFactory.createTicketFirstZone('r_20')
        self.btn_reduced_40 = self.buttonsFactory.createTicketFirstZone('r_40')
        self.btn_reduced_oneway = self.buttonsFactory.createTicketFirstZone('r_oneway')
        self.btn_reduced_twoway = self.buttonsFactory.createTicketFirstZone('r_twoway')
        self.widget_reduced_first = self.widgetFactory.createWidget(self.TicketsWidget, 'widget_reduced_first')
        self.grid_reduced_tickets_first = self.gridFactory.createGrid( self.widget_reduced_first,'zone1','r',[
            self.btn_reduced_20, self.btn_reduced_40, self.btn_reduced_oneway, self.btn_reduced_twoway
        ])

        # NORMAL ZONE 1
        self.btn_normal_20 = self.buttonsFactory.createTicketFirstZone('n_20')
        self.btn_normal_40 = self.buttonsFactory.createTicketFirstZone('n_40')
        self.btn_normal_oneway = self.buttonsFactory.createTicketFirstZone('n_oneway')
        self.btn_normal_twoway = self.buttonsFactory.createTicketFirstZone('n_twoway')
        self.widget_normal_first = self.widgetFactory.createWidget(self.TicketsWidget, 'widget_normal_first')
        self.grid_normal_tickets_first = self.gridFactory.createGrid( self.widget_normal_first,'zone1','n',[
            self.btn_normal_20, self.btn_normal_40, self.btn_normal_oneway, self.btn_normal_twoway
        ])

        # REDUCED ZONE 2
        self.btn_reduced_20_2 = self.buttonsFactory.createTicketSecondZone('r_20')
        self.btn_reduced_40_2 = self.buttonsFactory.createTicketSecondZone('r_40')
        self.btn_reduced_oneway_2 = self.buttonsFactory.createTicketSecondZone('r_oneway')
        self.btn_reduced_twoway_2 = self.buttonsFactory.createTicketSecondZone('r_twoway')
        self.widget_reduced_second = self.widgetFactory.createWidget(self.TicketsWidget, 'widget_reduced_second')
        self.grid_reduced_tickets_second = self.gridFactory.createGrid( self.widget_reduced_second,'zone2','r',[
            self.btn_reduced_20_2, self.btn_reduced_40_2, self.btn_reduced_oneway_2, self.btn_reduced_twoway_2
        ])

        # NORMAL ZONE 2
        self.btn_normal_20_2 = self.buttonsFactory.createTicketSecondZone('n_20')
        self.btn_normal_40_2 = self.buttonsFactory.createTicketSecondZone('n_40')
        self.btn_normal_oneway_2 = self.buttonsFactory.createTicketSecondZone('n_oneway')
        self.btn_normal_twoway_2 = self.buttonsFactory.createTicketSecondZone('n_twoway')
        self.widget_normal_second = self.widgetFactory.createWidget(self.TicketsWidget, 'widget_normal_second')
        self.grid_normal_tickets_second = self.gridFactory.createGrid( self.widget_normal_second,'zone2','n',[
            self.btn_normal_20_2, self.btn_normal_40_2, self.btn_normal_oneway_2, self.btn_normal_twoway_2
        ])

    def generateCosmetics(self):
        self.line = QtWidgets.QFrame(self.TicketsWidget)
        self.line.setGeometry(QtCore.QRect(0, 100, 951, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.TicketsWidget)
        self.line_2.setGeometry(QtCore.QRect(0, 380, 951, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.TicketsWidget)
        self.line_3.setGeometry(QtCore.QRect(0, 640, 951, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.TicketsWidget)
        self.line_4.setGeometry(QtCore.QRect(263, 650, 20, 101))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.TicketsWidget)
        self.line_5.setGeometry(QtCore.QRect(940, 0, 20, 731))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.TicketsWidget)
        self.line_6.setGeometry(QtCore.QRect(590, 650, 20, 91))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.TicketsWidget)
        self.line_7.setGeometry(QtCore.QRect(483, 110, 20, 541))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
