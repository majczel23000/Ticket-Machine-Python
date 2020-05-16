from model.Label import Label


class LabelFactory:
    def createLabel(self, parent, name, geometry=0, font=0, alignment=0, text=0):
        return Label(parent, name, geometry, font, alignment, text)