from view.model.Grid import Grid
from view.static.grid_data import gridsData


class GridFactory:
    def createGrid(self, parent, zone, code, items):
        return Grid(parent, gridsData[zone][code]['name'], items).grid
