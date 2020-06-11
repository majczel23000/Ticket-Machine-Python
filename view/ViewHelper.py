from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QGridLayout, QWidget


class ViewHelper:

    @staticmethod
    def find_button_by_object_name(view, obj_name):
        return view.findChild(QPushButton, obj_name)

    @staticmethod
    def find_label_by_object_name(view, obj_name):
        return view.findChild(QLabel, obj_name)

    @staticmethod
    def find_QVBoxLayout_by_object_name(view, obj_name):
        return view.findChild(QVBoxLayout, obj_name)

    @staticmethod
    def find_QGridLayout_by_object_name(view, obj_name):
        return view.findChild(QGridLayout, obj_name)

    @staticmethod
    def find_QWidget_by_object_name(view, obj_name):
        return view.findChild(QWidget, obj_name)
