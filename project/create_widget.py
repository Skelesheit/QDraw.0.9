import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QWidget, QDialog, QColorDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from CreateList_design import Ui_Form


class wdg_create_list(Ui_Form, QWidget):
    def __init__(self):
        super(wdg_create_list, self).__init__()
        self.setupUi(self)
        self.init_Ui()

    def init_Ui(self):
        self.pushButton.clicked.connect(self.create_picture())

    def create_picture(self):
        length = self.spinBox.value()
        width = self.spinBox_2.value()
        name = self.lineEdit.text()
        self.destroy()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Work = wdg_create_list()
    Work.show()
    sys.exit(app.exec())
