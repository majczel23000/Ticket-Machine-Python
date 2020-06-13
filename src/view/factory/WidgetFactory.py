from src.view.model.Widget import Widget
from src.view.static.widget_data import widgetData


class WidgetFactory:
    """
    Factory class for creating Widget objects
    """

    def createWidget(self, parent, code):
        """
        Creating Widget object
        :param parent: parent where widget will be inserted
        :param code: widget code
        :return: Widget class object
        """
        return Widget(parent, widgetData[code]['geometry'], widgetData[code]['name'])
