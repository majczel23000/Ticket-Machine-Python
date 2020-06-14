import sys
import unittest
from PyQt5 import QtWidgets, QtCore
from src.view.model.Button import Button


class ButtonTest(unittest.TestCase):

    __button = None
    button_name = 'button_test'
    icon_size = QtCore.QSize(200, 100)
    button_icon = {"icon": "src/assets/10.00.png", "iconSize": icon_size}
    button_text = 'button_text'

    @classmethod
    def setUp(cls):
        app = QtWidgets.QApplication(sys.argv)
        cls.__button = Button(cls.button_name, cls.button_text, cls.button_icon, 0)

    def test_button_instance(self):
        self.assertIsInstance(self.__button, QtWidgets.QPushButton)

    def test_button_object_name(self):
        self.assertEqual(self.__button.objectName(), self.button_name)

    def test_button_text(self):
        self.assertEqual(self.__button.text(), self.button_text)

    def test_button_icon_size(self):
        self.assertEqual(self.__button.iconSize(), self.icon_size)


if __name__ == '__main__':
    unittest.main()
