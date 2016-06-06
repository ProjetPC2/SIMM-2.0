import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ListViewExample(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.createGUI()

    def createGUI(self):
        #donnees test sous forme d'une liste de tuple
        tableData = [
            ("123", 'table', "a"),
            ("456", 'chaise', "b"),
            ("789", 'toto', "c")
        ]

        #creation d'une table widget de taille 3x3
        table = QTableWidget(3, 3)
        #on met les titres des colonnes
        table.setHorizontalHeaderLabels(["ID", "Categorie equipement", "Marque"])
        table.resize(150, 50)

        #remplissage du tableau
        for i, (name, color, lettre) in enumerate(tableData):
            #Creation des QTableWidgetItem
            nameItem = QTableWidgetItem(name)
            colorItem = QTableWidgetItem(color)
            lettreItem = QTableWidgetItem(lettre)
            #Insertion des elements
            table.setItem(i, 0, nameItem)
            table.setItem(i, 1, colorItem)
            table.setItem(i, 2, lettreItem)
        # table.resizeColumnToContents(0)
        # On fait en sorte que la table prend la largeur de la fenetre
        table.horizontalHeader().setStretchLastSection(True)

        layout = QGridLayout()
        layout.addWidget(table, 0, 0)
        self.setLayout(layout)

        self.setGeometry(200, 100, 200, 1000)
        self.resize(1000, 1000)
        self.setWindowTitle("SIMM 2.0")
        self.setWindowIcon(QIcon('PC2.png'))

if __name__ == "__main__":
    a = QApplication(sys.argv)
    f = ListViewExample()
    f.show()
    a.exec_()