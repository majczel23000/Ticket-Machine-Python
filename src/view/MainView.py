from PyQt5 import QtWidgets

from src.view.ConfirmationView import ConfirmationView
from src.view.TicketsView import TicketsView
from src.view.PaymentView import PaymentView


class MainView(QtWidgets.QMainWindow):
    """
    Main view class of QMainWindow type
    """

    def __init__(self):
        """
        The constructor of main view class which set up: current_view, tickets_view, confirmation_view, payment_view
        """
        super(MainView, self).__init__()
        self.tickets_view = TicketsView()
        self.payment_view = None
        self.confirmation_view = None
        self.setCentralWidget(self.tickets_view)
        self.setWindowTitle("AUTOMAT BILETOWY RP. Michał Raźny, Piotr Pindel, 41K9")
        self.setStyleSheet("QMainWindow {background: '#A8CDE6';}")
        self.resize(920, 720)
        self.show()

    def change_view(self, view):
        """
        Change view based on parameter view
        :param view: view name to change
        """
        if view == "payment":
            if self.tickets_view.isVisible():
                self.tickets_view.setVisible(False)
            self.payment_view = PaymentView()
            self.setCentralWidget(self.payment_view)
            self.payment_view.setVisible(True)
        elif view == "confirmation":
            if self.payment_view.isVisible():
                self.payment_view.setVisible(False)
            self.confirmation_view = ConfirmationView()
            self.setCentralWidget(self.confirmation_view)
            self.confirmation_view.setVisible(True)
        elif view == "tickets":
            if self.confirmation_view.isVisible():
                self.confirmation_view.setVisible(False)
            self.tickets_view = TicketsView()
            self.setCentralWidget(self.tickets_view)
            self.tickets_view.setVisible(True)
