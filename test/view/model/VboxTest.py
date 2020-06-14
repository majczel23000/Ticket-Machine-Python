import sys
import unittest
from PyQt5 import QtWidgets
from src.view.model.Vbox import Vbox


class VboxTest(unittest.TestCase):

    __vbox = None
    vbox_name = 'vbox_test'

    @classmethod
    def setUp(cls):
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        widget = QtWidgets.QWidget()
        window.setCentralWidget(widget)
        cls.__vbox = Vbox(widget, cls.vbox_name, list()).vbox

    def test_vbox_instance(self):
        self.assertIsInstance(self.__vbox, QtWidgets.QVBoxLayout)

    def test_vbox_object_name(self):
        self.assertEqual(self.__vbox.objectName(), self.vbox_name)


if __name__ == '__main__':
    unittest.main()
