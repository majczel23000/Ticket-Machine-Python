from model.IMoney import IMoney


class Banknote(IMoney):

    def get_value(self):
        return self.value
