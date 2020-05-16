from model.Vbox import Vbox


class VboxFactory:
    def createVbox(self, parent, name, items):
        return Vbox(parent, name, items).vbox
