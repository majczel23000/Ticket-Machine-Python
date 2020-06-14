import sys
import unittest
from PyQt5 import QtWidgets
from src.view.model.Grid import Grid


class GridTest(unittest.TestCase):

    __grid = None
    grid_name = 'grid_test'

    @classmethod
    def setUp(cls):
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        widget = QtWidgets.QWidget()
        window.setCentralWidget(widget)
        cls.__grid = Grid(widget, cls.grid_name, list()).grid

    def test_grid_instance(self):
        self.assertIsInstance(self.__grid, QtWidgets.QGridLayout)

    def test_grid_object_name(self):
        self.assertEqual(self.__grid.objectName(), self.grid_name)


if __name__ == '__main__':
    unittest.main()
