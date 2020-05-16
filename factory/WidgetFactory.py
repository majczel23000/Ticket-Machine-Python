from model.Widget import Widget
from common.widget_data import widgetData


class WidgetFactory:
    def createWidget(self, parent, code):
        return Widget(parent, widgetData[code]['geometry'], widgetData[code]['name'])