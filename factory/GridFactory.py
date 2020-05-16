from model.Grid import Grid
from common.grid_data import gridsData


class GridFactory:
    def createGrid(self, parent, zone, code, items):
        return Grid(parent, gridsData[zone][code]['name'], items)
