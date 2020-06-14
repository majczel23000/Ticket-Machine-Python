import sys
import unittest
from PyQt5 import QtWidgets, QtCore
from src.view.model.Widget import Widget


class WidgetTest(unittest.TestCase):

    __widget = None
    widget_name = 'widget_test'
    widget_geometry = QtCore.QRect(0, 0, 10, 10)

    @classmethod
    def setUp(cls):
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        widget = QtWidgets.QWidget()
        window.setCentralWidget(widget)
        cls.__widget = Widget(widget, cls.widget_geometry, cls.widget_name)

    def test_widget_instance(self):
        self.assertIsInstance(self.__widget, QtWidgets.QWidget)

    def test_widget_object_name(self):
        self.assertEqual(self.__widget.objectName(), self.widget_name)

    def test_widget_geometry(self):
        self.assertEqual(self.__widget.geometry(), self.widget_geometry)


if __name__ == '__main__':
    unittest.main()
