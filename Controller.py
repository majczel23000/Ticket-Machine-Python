from PyQt5.QtWidgets import QLabel

from model.Order import *
from model.TicketMachine import *
from view.TicketsView import *
from factory.TicketFactory import TicketFactory

class Controller:
    def __init__(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        self.tickets_view = TicketsView()
        self.ticket_machine = TicketMachine()
        self.order = Order()
        self.ticketFactory = TicketFactory()
        self.assign_actions_to_buttons()
        sys.exit(app.exec_())

    # przypisanie clicków do poszczególnych buttonów
    def assign_actions_to_buttons(self):
        # Normalne I Strefa
        self.tickets_view.btn_normal_20_plus.clicked.connect(lambda: self.add_ticket(1, 2.00, 'normal', 'btn_normal_20_count', 'n20'))
        self.tickets_view.btn_normal_40_plus.clicked.connect(lambda: self.add_ticket(1, 3.60, 'normal', 'btn_normal_40_count', 'n40'))
        self.tickets_view.btn_normal_oneway_plus.clicked.connect(lambda: self.add_ticket(1, 4.00, 'normal', 'btn_normal_oneway_count', 'none'))
        self.tickets_view.btn_normal_twoway_plus.clicked.connect(lambda: self.add_ticket(1, 7.00, 'normal', 'btn_normal_twoway_count', 'ntwo'))

        self.tickets_view.btn_normal_20_minus.clicked.connect(lambda: self.remove_ticket('n20', 'btn_normal_20_count'))
        self.tickets_view.btn_normal_40_minus.clicked.connect(lambda: self.remove_ticket('n40', 'btn_normal_40_count'))
        self.tickets_view.btn_normal_oneway_minus.clicked.connect(lambda: self.remove_ticket('none', 'btn_normal_oneway_count'))
        self.tickets_view.btn_normal_twoway_minus.clicked.connect(lambda: self.remove_ticket('ntwo', 'btn_normal_twoway_count'))

        #Normalne II Strefa
        self.tickets_view.btn_normal_20_2_plus.clicked.connect(lambda: self.add_ticket(2, 2.50, 'normal', 'btn_normal_20_2_count', 'n20_2'))
        self.tickets_view.btn_normal_40_2_plus.clicked.connect(lambda: self.add_ticket(2, 4.00, 'normal', 'btn_normal_40_2_count', 'n40_2'))
        self.tickets_view.btn_normal_oneway_2_plus.clicked.connect(lambda: self.add_ticket(2, 4.80, 'normal', 'btn_normal_oneway_2_count', 'none_2'))
        self.tickets_view.btn_normal_twoway_2_plus.clicked.connect(lambda: self.add_ticket(2, 7.50, 'normal', 'btn_normal_twoway_2_count', 'ntwo_2'))

        self.tickets_view.btn_normal_20_2_minus.clicked.connect(lambda: self.remove_ticket('n20_2', 'btn_normal_20_2_count'))
        self.tickets_view.btn_normal_40_2_minus.clicked.connect(lambda: self.remove_ticket('n40_2', 'btn_normal_40_2_count'))
        self.tickets_view.btn_normal_oneway_2_minus.clicked.connect(lambda: self.remove_ticket('none_2', 'btn_normal_oneway_2_count'))
        self.tickets_view.btn_normal_twoway_2_minus.clicked.connect(lambda: self.remove_ticket('ntwo_2', 'btn_normal_twoway_2_count'))

        # Ulgowe I Strefa
        self.tickets_view.btn_reduced_20_plus.clicked.connect(lambda: self.add_ticket(1, 1.00, 'reduced', 'btn_reduced_20_count', 'r20'))
        self.tickets_view.btn_reduced_40_plus.clicked.connect(lambda: self.add_ticket(1, 1.80, 'reduced', 'btn_reduced_40_count', 'r40'))
        self.tickets_view.btn_reduced_oneway_plus.clicked.connect(lambda: self.add_ticket(1, 2.00, 'reduced', 'btn_reduced_oneway_count', 'rone'))
        self.tickets_view.btn_reduced_twoway_plus.clicked.connect(lambda: self.add_ticket(1, 3.50, 'reduced', 'btn_reduced_twoway_count', 'rtwo'))

        self.tickets_view.btn_reduced_20_minus.clicked.connect(lambda: self.remove_ticket('r20', 'btn_reduced_20_count'))
        self.tickets_view.btn_reduced_40_minus.clicked.connect(lambda: self.remove_ticket('r40', 'btn_reduced_40_count'))
        self.tickets_view.btn_reduced_oneway_minus.clicked.connect(lambda: self.remove_ticket('rone', 'btn_reduced_oneway_count'))
        self.tickets_view.btn_reduced_twoway_minus.clicked.connect(lambda: self.remove_ticket('rtwo', 'btn_reduced_twoway_count'))

        # Ulgowe II Strefa
        self.tickets_view.btn_reduced_20_2_plus.clicked.connect(lambda: self.add_ticket(2, 1.20, 'reduced', 'btn_reduced_20_2_count', 'r20_2'))
        self.tickets_view.btn_reduced_40_2_plus.clicked.connect(lambda: self.add_ticket(2, 2.00, 'reduced', 'btn_reduced_40_2_count', 'r40_2'))
        self.tickets_view.btn_reduced_oneway_2_plus.clicked.connect(lambda: self.add_ticket(2, 2.50, 'reduced', 'btn_reduced_oneway_2_count', 'rone_2'))
        self.tickets_view.btn_reduced_twoway_2_plus.clicked.connect(lambda: self.add_ticket(2, 4.00, 'reduced', 'btn_reduced_twoway_2_count', 'rtwo_2'))

        self.tickets_view.btn_reduced_20_2_minus.clicked.connect(lambda: self.remove_ticket('r20_2', 'btn_reduced_20_2_count'))
        self.tickets_view.btn_reduced_40_2_minus.clicked.connect(lambda: self.remove_ticket('r40_2', 'btn_reduced_40_2_count'))
        self.tickets_view.btn_reduced_oneway_2_minus.clicked.connect(lambda: self.remove_ticket('rone_2', 'btn_reduced_oneway_2_count'))
        self.tickets_view.btn_reduced_twoway_2_minus.clicked.connect(lambda: self.remove_ticket('rtwo_2', 'btn_reduced_twoway_2_count'))

        # przejście do płatności
        self.tickets_view.payment.clicked.connect(lambda: self.go_to_payment_view())

    def add_ticket(self, zone_number, price, type, label, code):
        # get label with selected tickets count
        counter = self.tickets_view.findChild(QLabel, label)
        counter_int = int(counter.text())
        counter_int += 1
        counter.setText(str(counter_int))
        # create proper ticket by ticket factory
        t = self.ticketFactory.createTicket(type, zone_number, price, code)
        self.order.add_ticket(t)
        self.update_informations()

    def update_informations(self):
        self.tickets_view.label_tickets_count_value.setText(str(len(self.order.tickets)))
        self.tickets_view.label_total_cost_value.setText(str(self.order.cost))

    def remove_ticket(self, code, label):
        # search for specific ticket in list
        if any(x.code == code for x in self.order.tickets):
            object_to_remove = next((x for x in self.order.tickets if x.code == code))
            self.order.tickets.remove(object_to_remove)
            self.order.cost -= object_to_remove.price
            self.order.cost = float(round(Decimal(self.order.cost), 2))
            self.update_informations()
            # reduce counter
            counter = self.tickets_view.findChild(QLabel, label)
            counter_int = int(counter.text())
            if counter_int > 0:
                counter_int -= 1
            counter.setText(str(counter_int))

    def go_to_payment_view(self):
        self.tickets_view.TicketsWidget.deleteLater()
