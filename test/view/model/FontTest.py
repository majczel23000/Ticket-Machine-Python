import sys
import unittest
from PyQt5 import QtWidgets, QtCore, QtGui
from src.view.model.Font import Font


class FontTest(unittest.TestCase):

    __font = None
    font_family = 'Consolas'
    font_size = 9
    font_bold = True
    font_italic = False
    font_weight = 75

    @classmethod
    def setUp(cls):
        app = QtWidgets.QApplication(sys.argv)
        cls.__font = Font(cls.font_family, cls.font_size, cls.font_bold, cls.font_italic, cls.font_weight)

    def test_font_instance(self):
        self.assertIsInstance(self.__font, QtGui.QFont)

    def test_font_family(self):
        self.assertEqual(self.__font.family(), self.font_family)

    def test_font_size(self):
        self.assertEqual(self.__font.pointSize(), self.font_size)

    def test_font_bold(self):
        self.assertEqual(self.__font.bold(), self.font_bold)

    def test_font_italic(self):
        self.assertEqual(self.__font.italic(), self.font_italic)

    def test_font_weight(self):
        self.assertEqual(self.__font.weight(), self.font_weight)


if __name__ == '__main__':
    unittest.main()
