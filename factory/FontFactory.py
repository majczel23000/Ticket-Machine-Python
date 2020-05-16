from model.Font import Font


class FontFactory:
    def createFont(self, family, size, bold, italic, weight):
        return Font(family, size, bold, italic, weight)