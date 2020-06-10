from PyQt5.QtWidgets import QPushButton, QLabel


class ViewHelper:

    @staticmethod
    def find_button_by_object_name(view, obj_name):
        return view.findChild(QPushButton, obj_name)

    @staticmethod
    def find_label_by_object_name(view, obj_name):
        return view.findChild(QLabel, obj_name)
