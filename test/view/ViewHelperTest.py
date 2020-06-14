import sys

from PyQt5 import QtWidgets

from src.view.ViewHelper import ViewHelper
import unittest


class ViewHelperTest(unittest.TestCase):
    __viewHelper = None
    __view = None
    button_name = 'button_test'
    label_name = 'label_test'
    qvbox_name = 'qvbox_test'
    qgrid_name = 'qgrid_test'
    qwidget_name = 'qwidget_test'

    @classmethod
    def setUp(cls):
        cls.__viewHelper = ViewHelper()

    def test_find_button_by_object_name(self):
        self.helper_create_view()
        self.assertIsInstance(self.__viewHelper.find_button_by_object_name(self.__view, self.button_name), QtWidgets.QPushButton)

    def test_find_label_by_object_name(self):
        self.helper_create_view()
        self.assertIsInstance(self.__viewHelper.find_label_by_object_name(self.__view, self.label_name), QtWidgets.QLabel)

    def test_find_QVBoxLayout_by_object_name(self):
        self.helper_create_view()
        self.assertIsInstance(self.__viewHelper.find_QVBoxLayout_by_object_name(self.__view, self.qvbox_name), QtWidgets.QVBoxLayout)

    def test_find_QWidget_by_object_name(self):
        self.helper_create_view()
        self.assertIsInstance(self.__viewHelper.find_QWidget_by_object_name(self.__view, self.qwidget_name), QtWidgets.QWidget)

    def helper_create_view(self):
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        widget = QtWidgets.QWidget()
        widget.setObjectName(self.qwidget_name)
        window.setCentralWidget(widget)
        btn = QtWidgets.QPushButton(widget)
        btn.setObjectName(self.button_name)
        label = QtWidgets.QLabel(widget)
        label.setObjectName(self.label_name)
        qvbox = QtWidgets.QVBoxLayout(widget)
        qvbox.setObjectName(self.qvbox_name)
        qgrid = QtWidgets.QGridLayout(widget)
        qgrid.setObjectName(self.qgrid_name)
        self.__view = window


if __name__ == '__main__':
    unittest.main()
