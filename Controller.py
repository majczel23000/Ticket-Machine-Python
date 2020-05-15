from PyQt5.QtWidgets import QLabel

from Order import *
from TicketMachine import *
from TicketsView import *
from Ticket import *


class Controller:
    def __init__(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        self.tickets_view = TicketsView()
        self.ticket_machine = TicketMachine()
        self.order = Order()
        self.assign_actions_to_buttons()
        sys.exit(app.exec_())

    # przypisanie clicków do poszczególnych buttonów
    def assign_actions_to_buttons(self):
        # Normalne I Strefa
        self.tickets_view.btn_normal_20_plus.clicked.connect(lambda: self.add_ticket('20 minutowy N 1', 2.00, 'Normalny', 'btn_normal_20_count'))
        self.tickets_view.btn_normal_40_plus.clicked.connect(lambda: self.add_ticket('40 minutowy  N 1', 3.60, 'Normalny', 'btn_normal_40_count'))
        self.tickets_view.btn_normal_oneway_plus.clicked.connect(lambda: self.add_ticket('Jednoprzejazdowy  N 1', 4.00, 'Normalny', 'btn_normal_oneway_count'))
        self.tickets_view.btn_normal_twoway_plus.clicked.connect(lambda: self.add_ticket('Dwuprzejazdowy  N 1', 7.00, 'Normalny', 'btn_normal_twoway_count'))

        self.tickets_view.btn_normal_20_minus.clicked.connect(lambda: self.remove_ticket('20 minutowy N 1', 'btn_normal_20_count'))
        self.tickets_view.btn_normal_40_minus.clicked.connect(lambda: self.remove_ticket('40 minutowy N 1', 'btn_normal_40_count'))
        self.tickets_view.btn_normal_oneway_minus.clicked.connect(lambda: self.remove_ticket('Jednoprzejazdowy N 1', 'btn_normal_oneway_count'))
        self.tickets_view.btn_normal_twoway_minus.clicked.connect(lambda: self.remove_ticket('Dwuprzejazdowy N 1', 'btn_normal_twoway_count'))

        #Normalne II Strefa
        self.tickets_view.btn_normal_20_2_plus.clicked.connect(lambda: self.add_ticket('20 minutowy N 2', 2.50, 'Normalny', 'btn_normal_20_2_count'))
        self.tickets_view.btn_normal_40_2_plus.clicked.connect(lambda: self.add_ticket('40 minutowy N 2', 4.00, 'Normalny', 'btn_normal_40_2_count'))
        self.tickets_view.btn_normal_oneway_2_plus.clicked.connect(lambda: self.add_ticket('Jednoprzejazdowy N 2', 4.80, 'Normalny', 'btn_normal_oneway_2_count'))
        self.tickets_view.btn_normal_twoway_2_plus.clicked.connect(lambda: self.add_ticket('Dwuprzejazdowy N 2', 7.50, 'Normalny', 'btn_normal_twoway_2_count'))

        self.tickets_view.btn_normal_20_2_minus.clicked.connect(lambda: self.remove_ticket('20 minutowy N 2', 'btn_normal_20_2_count'))
        self.tickets_view.btn_normal_40_2_minus.clicked.connect(lambda: self.remove_ticket('40 minutowy N 2', 'btn_normal_40_2_count'))
        self.tickets_view.btn_normal_oneway_2_minus.clicked.connect(lambda: self.remove_ticket('Jednoprzejazdowy N 2', 'btn_normal_oneway_2_count'))
        self.tickets_view.btn_normal_twoway_2_minus.clicked.connect(lambda: self.remove_ticket('Dwuprzejazdowy N 2', 'btn_normal_twoway_2_count'))

        # Ulgowe I Strefa
        self.tickets_view.btn_reduced_20_plus.clicked.connect(lambda: self.add_ticket('20 minutowy U 1', 1.00, 'Ulgowy', 'btn_reduced_20_count'))
        self.tickets_view.btn_reduced_40_plus.clicked.connect(lambda: self.add_ticket('40 minutowy U 1', 1.80, 'Ulgowy', 'btn_reduced_40_count'))
        self.tickets_view.btn_reduced_oneway_plus.clicked.connect(lambda: self.add_ticket('Jednoprzejazdowy U 1', 2.00, 'Ulgowy', 'btn_reduced_oneway_count'))
        self.tickets_view.btn_reduced_twoway_plus.clicked.connect(lambda: self.add_ticket('Dwuprzejazdowy U 1', 3.50, 'Ulgowy', 'btn_reduced_twoway_count'))

        self.tickets_view.btn_reduced_20_minus.clicked.connect(lambda: self.remove_ticket('20 minutowy U 1', 'btn_reduced_20_count'))
        self.tickets_view.btn_reduced_40_minus.clicked.connect(lambda: self.remove_ticket('40 minutowy U 1', 'btn_reduced_40_count'))
        self.tickets_view.btn_reduced_oneway_minus.clicked.connect(lambda: self.remove_ticket('Jednoprzejazdowy U 1', 'btn_reduced_oneway_count'))
        self.tickets_view.btn_reduced_twoway_minus.clicked.connect(lambda: self.remove_ticket('Dwuprzejazdowy U 1', 'btn_reduced_twoway_count'))

        # Ulgowe II Strefa
        self.tickets_view.btn_reduced_20_2_plus.clicked.connect(lambda: self.add_ticket('20 minutowy U 2', 1.20, 'Ulgowy', 'btn_reduced_20_2_count'))
        self.tickets_view.btn_reduced_40_2_plus.clicked.connect(lambda: self.add_ticket('40 minutowy U 2', 2.00, 'Ulgowy', 'btn_reduced_40_2_count'))
        self.tickets_view.btn_reduced_oneway_2_plus.clicked.connect(lambda: self.add_ticket('Jednoprzejazdowy U 2', 2.50, 'Ulgowy', 'btn_reduced_oneway_2_count'))
        self.tickets_view.btn_reduced_twoway_2_plus.clicked.connect(lambda: self.add_ticket('Dwuprzejazdowy U 2', 4.00, 'Ulgowy', 'btn_reduced_twoway_2_count'))

        self.tickets_view.btn_reduced_20_2_minus.clicked.connect(lambda: self.remove_ticket('20 minutowy U 2', 'btn_reduced_20_2_count'))
        self.tickets_view.btn_reduced_40_2_minus.clicked.connect(lambda: self.remove_ticket('40 minutowy U 2', 'btn_reduced_40_2_count'))
        self.tickets_view.btn_reduced_oneway_2_minus.clicked.connect(lambda: self.remove_ticket('Jednoprzejazdowy U 2', 'btn_reduced_oneway_2_count'))
        self.tickets_view.btn_reduced_twoway_2_minus.clicked.connect(lambda: self.remove_ticket('Dwuprzejazdowy U 2', 'btn_reduced_twoway_2_count'))


    # dodanie biletu do listy, zwiększenie licznika i update informacji
    def add_ticket(self, name, price, type, label):
        counter = self.tickets_view.findChild(QLabel, label)
        counter_int = int(counter.text())
        counter_int += 1
        counter.setText(str(counter_int))
        #print(name, price, type)
        t = Ticket(name, price, type)
        self.order.add_ticket(t)
        self.update_informations()

    # aktualizacja informacji o ilości i cenie wybranych biletów
    def update_informations(self):
        self.tickets_view.label_tickets_count_value.setText(str(len(self.order.tickets)))
        self.tickets_view.label_total_cost_value.setText(str(self.order.cost))

    #usuwanie biletu jeżeli istnieje w liście biletów i zmniejszenie countera
    def remove_ticket(self, name, label):
        # jeżeli jest w liscie
        if any(x.name == name for x in self.order.tickets):
            # odczytaj obiekt
            object_to_remove = next((x for x in self.order.tickets if x.name == name))
            self.order.tickets.remove(object_to_remove)
            self.order.cost -= object_to_remove.price
            self.order.cost = float(round(Decimal(self.order.cost), 2))
            self.update_informations()
            # zmniejsz licznik
            counter = self.tickets_view.findChild(QLabel, label)
            counter_int = int(counter.text())
            if counter_int>0:
                counter_int -= 1
            counter.setText(str(counter_int))
        else: # do wywalenia
            print("nie ma takiego biletu")

