

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon , QColor, QFont, QPainter, QPen
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QCoreApplication
from qtconsole.qt import QtCore

class AjoutEquipement(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(400, 175, 720, 700)
        self.setWindowTitle('SIMM 2.0 : Ajouter un équipement')
        self.setWindowIcon(QIcon('PC2.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AjoutEquipement()
    sys.exit(app.exec_())