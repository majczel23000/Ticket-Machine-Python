from Order import *
from TicketMachine import *
from TicketsView import *
from Ticket import *


class Controller:
    def __init__(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.tickets_view = TicketsView()
        self.tickets_view.setupUi(MainWindow)
        MainWindow.show()
        self.ticket_machine = TicketMachine()
        self.order = Order()
        self.assign_actions_to_buttons()
        sys.exit(app.exec_())

    # przypisanie clicków do poszczególnych buttonów
    def assign_actions_to_buttons(self):
        # Normalne I Strefa
        self.tickets_view.btn_normal_20.clicked.connect(lambda: self.add_ticket('20 minutowy', 2.00, 'Normalny'))
        self.tickets_view.btn_normal_40.clicked.connect(lambda: self.add_ticket('40 minutowy', 3.60, 'Normalny'))
        self.tickets_view.btn_normal_oneway.clicked.connect(lambda: self.add_ticket('Jednoprzejazdowy', 4.00, 'Normalny'))
        self.tickets_view.btn_normal_twoway.clicked.connect(lambda: self.add_ticket('Dwuprzejazdowy', 7.00, 'Normalny'))

        #Normalne II Strefa
        self.tickets_view.btn_normal_20_2.clicked.connect(lambda: self.add_ticket('20 minutowy', 2.50, 'Normalny'))
        self.tickets_view.btn_normal_40_2.clicked.connect(lambda: self.add_ticket('40 minutowy', 4.00, 'Normalny'))
        self.tickets_view.btn_normal_oneway_2.clicked.connect(lambda: self.add_ticket('Jednoprzejazdowy', 4.80, 'Normalny'))
        self.tickets_view.btn_normal_twoway_2.clicked.connect(lambda: self.add_ticket('Dwuprzejazdowy', 7.50, 'Normalny'))

        # Ulgowe I Strefa
        self.tickets_view.btn_reduced_20.clicked.connect(lambda: self.add_ticket('20 minutowy', 1.00, 'Ulgowy'))
        self.tickets_view.btn_reduced_40.clicked.connect(lambda: self.add_ticket('40 minutowy', 1.80, 'Ulgowy'))
        self.tickets_view.btn_reduced_oneway.clicked.connect(lambda: self.add_ticket('Jednoprzejazdowy', 2.00, 'Ulgowy'))
        self.tickets_view.btn_reduced_twoway.clicked.connect(lambda: self.add_ticket('Dwuprzejazdowy', 3.50, 'Ulgowy'))

        # Ulgowe II Strefa
        self.tickets_view.btn_reduced_20_2.clicked.connect(lambda: self.add_ticket('20 minutowy', 1.20, 'Ulgowy'))
        self.tickets_view.btn_reduced_40_2.clicked.connect(lambda: self.add_ticket('40 minutowy', 2.00, 'Ulgowy'))
        self.tickets_view.btn_reduced_oneway_2.clicked.connect(lambda: self.add_ticket('Jednoprzejazdowy', 2.50, 'Ulgowy'))
        self.tickets_view.btn_reduced_twoway_2.clicked.connect(lambda: self.add_ticket('Dwuprzejazdowy', 4.00, 'Ulgowy'))

    # dodanie biletu do listy czy cuś
    def add_ticket(self, name, price, type):
        print(name, price, type)
        t = Ticket(name, price, type)
        self.order.add_ticket(t)
