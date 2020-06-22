import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from src.factory.MoneyFactory import MoneyFactory
from src.model.Order import *
from src.model.TicketMachine import *
from src.factory.TicketFactory import TicketFactory
from src.view.MainView import *
from src.view.ViewHelper import ViewHelper
from src.pattern.decorators import delay
from src.view.factory.LabelsFactory import LabelFactory


class Controller:
    """
    Class of controller, which controls Ticket Machine
    """

    def __init__(self):
        """
        The constructor initializes the fields: app, ticket_machine, view_helper, order, ticketFactory, moneyFactory, labelFactory
        """
        app = QtWidgets.QApplication(sys.argv)
        self.ticket_machine = TicketMachine()
        self.view_helper = ViewHelper()
        self.order = Order()
        self.ticketFactory = TicketFactory()
        self.moneyFactory = MoneyFactory()
        self.labelFactory = LabelFactory()
        self.assing_ticket_actions()
        sys.exit(app.exec_())

    def assing_ticket_actions(self):
        """
        Assigning actions to buttons in view method
        :return: nothing
        """
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_normal_20_plus').clicked.connect(
            lambda: self.add_ticket(1, 2.00, 'normal', 'btn_normal_20_count', 'n20'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_normal_40_plus').clicked.connect(
            lambda: self.add_ticket(1, 3.60, 'normal', 'btn_normal_40_count', 'n40'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_normal_oneway_plus').clicked.connect(
            lambda: self.add_ticket(1, 4.00, 'normal', 'btn_normal_oneway_count',
                                    'none'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_normal_twoway_plus').clicked.connect(
            lambda: self.add_ticket(1, 7.00, 'normal', 'btn_normal_twoway_count',
                                    'ntwo'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_normal_20_minus').clicked.connect(
            lambda: self.remove_ticket('n20', 'btn_normal_20_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_normal_40_minus').clicked.connect(
            lambda: self.remove_ticket('n40', 'btn_normal_40_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_normal_oneway_minus').clicked.connect(
            lambda: self.remove_ticket('none', 'btn_normal_oneway_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_normal_twoway_minus').clicked.connect(
            lambda: self.remove_ticket('ntwo', 'btn_normal_twoway_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_normal_20_2_plus').clicked.connect(
            lambda: self.add_ticket(2, 2.50, 'normal', 'btn_normal_20_2_count', 'n20_2'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_normal_40_2_plus').clicked.connect(
            lambda: self.add_ticket(2, 4.00, 'normal', 'btn_normal_40_2_count', 'n40_2'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_normal_oneway_2_plus').clicked.connect(
            lambda: self.add_ticket(2, 4.80, 'normal', 'btn_normal_oneway_2_count',
                                    'none_2'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_normal_twoway_2_plus').clicked.connect(
            lambda: self.add_ticket(2, 7.50, 'normal', 'btn_normal_twoway_2_count',
                                    'ntwo_2'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_normal_20_2_minus').clicked.connect(
            lambda: self.remove_ticket('n20_2', 'btn_normal_20_2_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_normal_40_2_minus').clicked.connect(
            lambda: self.remove_ticket('n40_2', 'btn_normal_40_2_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_normal_oneway_2_minus').clicked.connect(
            lambda: self.remove_ticket('none_2', 'btn_normal_oneway_2_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_normal_twoway_2_minus').clicked.connect(
            lambda: self.remove_ticket('ntwo_2', 'btn_normal_twoway_2_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_reduced_20_plus').clicked.connect(
            lambda: self.add_ticket(1, 1.00, 'reduced', 'btn_reduced_20_count', 'r20'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_reduced_40_plus').clicked.connect(
            lambda: self.add_ticket(1, 1.80, 'reduced', 'btn_reduced_40_count', 'r40'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_reduced_oneway_plus').clicked.connect(
            lambda: self.add_ticket(1, 2.00, 'reduced', 'btn_reduced_oneway_count',
                                    'rone'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_reduced_twoway_plus').clicked.connect(
            lambda: self.add_ticket(1, 3.50, 'reduced', 'btn_reduced_twoway_count',
                                    'rtwo'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_reduced_20_minus').clicked.connect(
            lambda: self.remove_ticket('r20', 'btn_reduced_20_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_reduced_40_minus').clicked.connect(
            lambda: self.remove_ticket('r40', 'btn_reduced_40_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_reduced_oneway_minus').clicked.connect(
            lambda: self.remove_ticket('rone', 'btn_reduced_oneway_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_reduced_twoway_minus').clicked.connect(
            lambda: self.remove_ticket('rtwo', 'btn_reduced_twoway_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_reduced_20_2_plus').clicked.connect(
            lambda: self.add_ticket(2, 1.20, 'reduced', 'btn_reduced_20_2_count',
                                    'r20_2'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_reduced_40_2_plus').clicked.connect(
            lambda: self.add_ticket(2, 2.00, 'reduced', 'btn_reduced_40_2_count',
                                    'r40_2'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_reduced_oneway_2_plus').clicked.connect(
            lambda: self.add_ticket(2, 2.50, 'reduced',
                                    'btn_reduced_oneway_2_count', 'rone_2'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_reduced_twoway_2_plus').clicked.connect(
            lambda: self.add_ticket(2, 4.00, 'reduced',
                                    'btn_reduced_twoway_2_count', 'rtwo_2'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_reduced_20_2_minus').clicked.connect(
            lambda: self.remove_ticket('r20_2', 'btn_reduced_20_2_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_reduced_40_2_minus').clicked.connect(
            lambda: self.remove_ticket('r40_2', 'btn_reduced_40_2_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_reduced_oneway_2_minus').clicked.connect(
            lambda: self.remove_ticket('rone_2', 'btn_reduced_oneway_2_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(),
                                                    'btn_reduced_twoway_2_minus').clicked.connect(
            lambda: self.remove_ticket('rtwo_2', 'btn_reduced_twoway_2_count'))

        # przejście do płatności
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'payment').clicked.connect(
            lambda: self.change_view("payment"))

    def assign_payment_actions(self):
        """
        Assigning actions to payment buttons in payment view method.
        Assign actions to coins and banknotes objects.
        :return: nothing
        """
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_1_gr').clicked.connect(
            lambda: self.add_money("0.01", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_2_gr').clicked.connect(
            lambda: self.add_money("0.02", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_5_gr').clicked.connect(
            lambda: self.add_money("0.05", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_10_gr').clicked.connect(
            lambda: self.add_money("0.10", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_20_gr').clicked.connect(
            lambda: self.add_money("0.20", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_50_gr').clicked.connect(
            lambda: self.add_money("0.50", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_1_zl').clicked.connect(
            lambda: self.add_money("1.00", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_2_zl').clicked.connect(
            lambda: self.add_money("2.00", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_5_zl').clicked.connect(
            lambda: self.add_money("5.00", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_10_zl').clicked.connect(
            lambda: self.add_money("10.00", 'banknote'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_20_zl').clicked.connect(
            lambda: self.add_money("20.00", 'banknote'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_50_zl').clicked.connect(
            lambda: self.add_money("50.00", 'banknote'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_100_zl').clicked.connect(
            lambda: self.add_money("100.00", 'banknote'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_200_zl').clicked.connect(
            lambda: self.add_money("200.00", 'banknote'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_500_zl').clicked.connect(
            lambda: self.add_money("500.00", 'banknote'))

    def assign_confirmation_actions(self):
        """
        Assign actions to buttons in confirmation view
        """
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_again').clicked.connect(
            lambda: self.change_view("tickets"))

    def add_ticket(self, zone_number, price, type, label, code):
        """
        Adds ticket to chosen ticket list.
        :param zone_number: zone number of selected ticket
        :param price: price of selected ticket
        :param type: type of selected ticket
        :param label: label object name, which stores number of selected tickets
        :param code: code of ticket
        :return: nothing
        """
        counter = self.view_helper.find_label_by_object_name(self.ticket_machine.get_gui(), label)
        counter_int = int(counter.text())
        counter_int += 1
        counter.setText(str(counter_int))
        t = self.ticketFactory.createTicket(type, zone_number, price, code)
        self.order.add_ticket(t)
        self.update_informations()

    def remove_ticket(self, code, label):
        """
        Removes ticket from selected tickets list in order.
        :param label: label object name, which stores number of selected tickets
        :param code: code of ticket
        :return: nothing
        """
        if any(x.code == code for x in self.order.get_tickets()):
            object_to_remove = next((x for x in self.order.get_tickets() if x.code == code))
            self.order.tickets.remove(object_to_remove)
            self.order.set_cost(self.order.get_cost() - object_to_remove.price)
            self.order.set_cost(float(round(Decimal(self.order.get_cost()), 2)))
            self.update_informations()
            counter = self.view_helper.find_label_by_object_name(self.ticket_machine.get_gui(), label)
            counter_int = int(counter.text())
            if counter_int > 0:
                counter_int -= 1
            counter.setText(str(counter_int))

    def update_informations(self):
        """
        Update information about number of selected tickets and total cost.
        :return: nothing
        """
        self.view_helper.find_label_by_object_name(self.ticket_machine.get_gui(), "label_tickets_count_value").setText(
            str(len(self.order.get_tickets())))
        self.view_helper.find_label_by_object_name(self.ticket_machine.get_gui(), "label_total_cost_value").setText(
            str("{:.2f}".format(self.order.get_cost())) + " zł")

    def change_view(self, view_name):
        """
        Change view based on view_name.
        :param view_name: name of view to change
        :return: nothing
        """
        if view_name == "payment" and len(self.order.get_tickets()) > 0:
            self.ticket_machine.get_gui().change_view(view_name)
            self.assign_payment_actions()
            self.view_helper.find_label_by_object_name(self.ticket_machine.get_gui(),
                                                       "label_payment_left_value").setText(
                str("{:.2f}".format(self.order.get_cost())) + " zł")
            self.view_helper.find_label_by_object_name(self.ticket_machine.get_gui(), "label_ticket_count").setText(
                str(len(self.order.get_tickets())))
            self.view_helper.find_label_by_object_name(self.ticket_machine.get_gui(),
                                                       "label_payment_change_value").setText(
                str("{:.2f}".format(self.order.get_cost())) + " zł")

        elif view_name == "confirmation":
            self.ticket_machine.get_gui().change_view(view_name)
            self.assign_confirmation_actions()
        elif view_name == "tickets":
            self.ticket_machine.get_gui().change_view(view_name)
            self.assing_ticket_actions()

    def add_money(self, value, money_type):
        """
        Create inserted money object and add it to inserted money list.
        If total inserted value is greater than total cost, it calls method to calculate and return change.
        :param value: value of money
        :param money_type: type of money
        :return: nothing
        """
        money = self.moneyFactory.createMoney(money_type, value)
        self.order.insert_money(money)

        inserted = self.order.get_inserted_amount()
        remained = self.order.get_cost()
        left_to_pay = round(remained - inserted, 2)

        self.view_helper.find_label_by_object_name(self.ticket_machine.get_gui(), "label_payment_left_value").setText(
            str("{:.2f}".format(left_to_pay)) + " zł")

        if self.order.get_inserted_amount() >= self.order.get_cost():
            self.change_view("confirmation")
            self.order.calculate_exchange()
            self.return_tickets_and_change()

    def return_tickets_and_change(self):
        """
        Generates bought tickets and generate change.
        :return: nothing
        """

        cash = self.order.get_change_list()
        tickets: list() = self.order.get_tickets()
        cash_layout = self.view_helper.find_QGridLayout_by_object_name(self.ticket_machine.get_gui(),
                                                                       "grid_your_change")
        tickets_scroll: QVBoxLayout = self.view_helper.find_QWidget_by_object_name(self.ticket_machine.get_gui(),
                                                                                   "scroll_your_tickets")
        tickets_layout = QtWidgets.QVBoxLayout(tickets_scroll)
        i = 1
        for ticket in tickets:
            label = self.labelFactory.createTicketLabel('ticket', ticket.get_info())
            tickets_layout.addWidget(label)
            label.setVisible(False)
            self.print_tickets(label)

        for money in cash:
            label = QLabel()
            pixmap = QPixmap('assets/' + "{:.2f}".format(money) + '.png')
            label.setPixmap(pixmap)
            if money > 5:
                label.setMaximumSize(150, 80)
            else:
                label.setMaximumSize(80, 80)
            label.setScaledContents(True)
            label.setVisible(False)
            self.give_change(cash_layout, label, i)
            i += 1
        self.order.clear_order_data()

    @delay(2.0)
    def print_tickets(self, label):
        """
        Print ticket to bought ticket list. Simulate waiting proccess with delay decorator.
        :return: nothing
        """
        label.setVisible(True)
        self.view_helper.find_label_by_object_name(self.ticket_machine.get_gui(), 'label_thanks').show()
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_again').setDisabled(False)

    @delay(2.0)
    def give_change(self, cash_layout, label, i):
        if i < 5:
            cash_layout.addWidget(label, i, 0, 1, 1)
        elif i < 9:
            cash_layout.addWidget(label, i - 4, 1, 1, 1)
        else:
            cash_layout.addWidget(label, i - 8, 2, 1, 1)
        label.setVisible(True)
