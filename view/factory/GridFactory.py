from view.model.Grid import Grid
from view.static.grid_data import gridsData


class GridFactory:
    """
    Factory class for creating Grid objects
    """

    def createGrid(self, parent, zone, code, items):
        """
        Creating Grid object
        :param parent: parent where grid will be inserted
        :param zone: zone number
        :param code: grid code
        :param items: list of items to insert into grid
        :return: Grid class object
        """
        return Grid(parent, gridsData[zone][code]['name'], items).grid
