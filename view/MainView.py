from PyQt5 import QtCore, QtWidgets
from view.TicketsView import TicketsView
from PaymentView import PaymentView

class MainView(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        self.current_view = "tickets_view"
        self.tickets_view = TicketsView()
        self.payment_view = PaymentView()
        self.setCentralWidget(self.tickets_view)
        self.setWindowTitle("Biletomat razpin")
        self.setStyleSheet("QMainWindow {background: 'white';}")
        self.resize(950, 732)
        self.show()

    def change_view(self, view):
        if view == "payment":
            if self.current_view == "tickets_view":
                self.tickets_view.deleteLater()
            self.setCentralWidget(self.payment_view)
