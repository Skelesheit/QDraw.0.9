import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QWidget, QDialog, QColorDialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Qdrow(QWidget):
    def __init__(self):
        super(Qdrow, self).__init__()
        self.setGeometry(200, 200, 500, 500)
        self.init_UI()

    def init_UI(self):
        self.QL = QLabel(self)
        self.QL.setGeometry(200, 200, 100, 100)
        self.QL.show()
        self.QL.setText("aaaaaaaa")
        self.QL.show()
        self.QL.hide()
        self.QL.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Work = Qdrow()
    Work.show()
    sys.exit(app.exec())
