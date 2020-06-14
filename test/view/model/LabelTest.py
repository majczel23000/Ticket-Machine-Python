import sys
import unittest
from PyQt5 import QtWidgets, QtCore
from src.view.model.Label import Label


class LabelTest(unittest.TestCase):

    __label = None
    label_name = 'label_test'
    label_geometry = QtCore.QRect(0, 0, 10, 10)
    label_text = 'label_text'
    label_alignment = QtCore.Qt.AlignCenter

    @classmethod
    def setUp(cls):
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        widget = QtWidgets.QWidget()
        window.setCentralWidget(widget)
        cls.__label = Label(widget, cls.label_name, cls.label_geometry, 0, cls.label_alignment, cls.label_text, 0)

    def test_label_instance(self):
        self.assertIsInstance(self.__label, QtWidgets.QLabel)

    def test_label_object_name(self):
        self.assertEqual(self.__label.objectName(), self.label_name)

    def test_label_geometry(self):
        self.assertEqual(self.__label.geometry(), self.label_geometry)

    def test_label_text(self):
        self.assertEqual(self.__label.text(), self.label_text)

    def test_label_alignment(self):
        self.assertEqual(self.__label.alignment(), self.label_alignment)


if __name__ == '__main__':
    unittest.main()
