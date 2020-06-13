from src.view.model.Vbox import Vbox


class VboxFactory:
    """
    Factory class for creating Vbox objects
    """

    def createVbox(self, parent, name, items):
        """
        Creating Vbox object
        :param parent: parent where vbox will be inserted
        :param name: vbox name
        :param items: list of items to be inserted into vbox
        :return: Vbox class object
        """
        return Vbox(parent, name, items).vbox
