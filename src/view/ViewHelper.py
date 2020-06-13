from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QGridLayout, QWidget


class ViewHelper:
    """
    View helper class
    """

    @staticmethod
    def find_button_by_object_name(view, obj_name):
        """
        Static method to find button object from view by its name
        :param view: view object
        :param obj_name: object name to find
        :return: found object
        """
        return view.findChild(QPushButton, obj_name)

    @staticmethod
    def find_label_by_object_name(view, obj_name):
        """
        Static method to find label object from view by its name
        :param view: view object
        :param obj_name: object name to find
        :return: found object
        """
        return view.findChild(QLabel, obj_name)

    @staticmethod
    def find_QVBoxLayout_by_object_name(view, obj_name):
        """
        Static method to find QVBoxLayout object from view by its name
        :param view: view object
        :param obj_name: object name to find
        :return: found object
        """
        return view.findChild(QVBoxLayout, obj_name)

    @staticmethod
    def find_QGridLayout_by_object_name(view, obj_name):
        """
        Static method to find QGridLayout object from view by its name
        :param view: view object
        :param obj_name: object name to find
        :return: found object
        """
        return view.findChild(QGridLayout, obj_name)

    @staticmethod
    def find_QWidget_by_object_name(view, obj_name):
        """
        Static method to find QWidget object from view by its name
        :param view: view object
        :param obj_name: object name to find
        :return: found object
        """
        return view.findChild(QWidget, obj_name)
