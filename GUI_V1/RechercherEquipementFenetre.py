"""
Fichier de création d'une fenêtre de recherche d'un équipement :
"""
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import *
from qtconsole.qt import QtCore
from PyQt5.QtGui import QIcon, QFont
from AbstractWindow import AbstractWindow
class ListeDefilante():
    listeCategorieEquip = ["Categorie1", "Categorie2", "Categorie3"]
    listeEtatService = ["En service", "En maintenance", "Au rebus"]
    listeCentreService = ["Centre 1", "Centre 2", "Centre 3"]
    listeSalle = ["Chambre patient", "Salle d'operation", "Salle de reunion"]
    listeProvenance = ["CHU Ste-Justine", "Provenance 2", "Provenance 3"]


class RerchercherEquipementFenetre(QDialog, AbstractWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.rechercher()

    def initUI(self):
        self.widgetList = list()
        #self.window.colorFont('red')

        self.setWindowIcon(QIcon('web.png'))

        self.Titre = QLabel('Assistant de recherche - Équipement')
        self.Titre.setFont((QFont('SansSerif', 24)))
        #self.Titre.setIcon(QtGui.QIcon("loupe.png"))
        #self.Titre.setIconSize(QtCore.QSize(50, 50))

        NoSerieLabel = QLabel('Numéro de série')
        NoSerieEdit = QLineEdit()

        CategorieEquipLabel = QLabel("Catégorie d'équipement")
        CategorieEquipComboBox = QComboBox()
        for equipement in ListeDefilante.listeCategorieEquip:
            CategorieEquipComboBox.addItem(equipement)

        EtatServiceLabel = QLabel('État de service')
        EtatServiceComboBox = QComboBox()
        for etat in ListeDefilante.listeEtatService:
            EtatServiceComboBox.addItem(etat)

        CentreServiceLabel = QLabel('Centre de service')
        CentreServiceComboBox = QComboBox()
        for centre in ListeDefilante.listeCentreService:
            CentreServiceComboBox.addItem(centre)

        SalleLabel = QLabel('Salle')
        SalleComboBox = QComboBox()
        for salle in ListeDefilante.listeSalle:
            SalleComboBox.addItem(salle)

        ProvenanceLabel = QLabel('Provenance')
        ProvenanceComboBox = QComboBox()
        for provenance in ListeDefilante.listeProvenance:
            ProvenanceComboBox.addItem(provenance)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.Titre, 1, 0)

        grid.addWidget(CategorieEquipLabel, 2, 0)
        grid.addWidget(CategorieEquipComboBox, 3, 0)

        grid.addWidget(NoSerieLabel, 2, 1)
        grid.addWidget(NoSerieEdit, 3, 1)


        grid.addWidget(EtatServiceLabel, 4, 0)
        grid.addWidget(EtatServiceComboBox, 5, 0)

        grid.addWidget(CentreServiceLabel, 4, 1)
        grid.addWidget(CentreServiceComboBox, 5, 1)


        grid.addWidget(SalleLabel, 6, 0)
        grid.addWidget(SalleComboBox, 7, 0)

        grid.addWidget(ProvenanceLabel, 6, 1)
        grid.addWidget(ProvenanceComboBox, 7, 1)

        quitButton = QPushButton("Quitter")
        grid.addWidget(quitButton, 12, 1)
        # quitButton.clicked.connect(QCoreApplication.instance().quit)
        quitButton.clicked.connect(self.quitter)
        self.setLayout(grid)

        self.setGeometry(300, 300, 700, 300)
        self.setWindowTitle('Projet PC2')
        self.show()

        # donnees teste sous forme d'un liste de tuple
        self.tableData = [
            ("123", 'self.table', "a"),
            ("456", 'chaise', "b"),
            ("789", 'toto', "c")
            ]

        # creation d'une self.table widget de taille 3x3
        self.table = QTableWidget()
        # self.table.si
           # on met les titres des colonnes
        self.table.setHorizontalHeaderLabels(["ID", "Catégorie d'équipement", "Marque"])
        self.table.resize(300, 100)
        self.table.resizeColumnsToContents()
        # remplissage du tableau

            #layout = QGridLayout()
        grid.addWidget(self.table, 10, 0)
        self.resize(1000, 1000)
            #self.setLayout(layout)

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()

    def quitter(self):
        reply = QMessageBox.question(self, 'Message',
                                     "Etes-vous sur de vouloir quitter ?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # self.hide()
            # self.close()
            self.destroy()

    def center(self):
        """Methode permettant de centrer la fenetre"""
        # Nous recuperons la geometrie de la fenetre principale
        qr = self.frameGeometry()
        # Nous recuperons la definition de l'ecran et nous recuperons le point central
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        # self.move(qr.center)

    def rechercher(self):
        self.tableData = [
            ("123", 'self.table', "a"),
            ("456", 'chaise', "b"),
            ("789", 'toto', "c")
        ]
        # self.tableData.append()
        self.table.setRowCount(len(self.tableData))
        self.table.setColumnCount(10)
        self.table.setHorizontalHeaderLabels(["ID", "Catégorie d'équipement", "Marque", "No de serie",
                                              "Salle", "Centre de service", "Date Acquisition", "Date dernier entretien",
                                              "Provenance", "Etat de service", "Etat de conservation", "Commentaires"])
        self.table.resizeColumnsToContents()

        # self.table.setCol

        for i, (name, color, lettre) in enumerate(self.tableData):
            # Creation des QTableWidgetItem
            nameItem = QTableWidgetItem(name)
            colorItem = QTableWidgetItem(color)
            lettreItem = QTableWidgetItem(lettre)
            # Insertion des elements
            self.table.setItem(i, 0, nameItem)
            self.table.setItem(i, 1, colorItem)
            self.table.setItem(i, 2, lettreItem)
        # for i, (name, color, lettre) in enumerate(self.tableData):
        #     # Creation des QTableWidgetItem
        #     # nameItem = QTableWidgetItem(name)
        #     # colorItem = QTableWidgetItem(color)
        #     # lettreItem = QTableWidgetItem(lettre)
        #     # # Insertion des elements
        #     self.table.setItem(i, 3, nameItem)
        #     self.table.setItem(i, 4, colorItem)
        #     self.table.setItem(i, 5, lettreItem)
        # self.table.resizeColumnToContents(0)
        # On fait en sorte que la self.table prend la largeur de la fenetre
        self.table.horizontalHeader().setStretchLastSection(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RerchercherEquipementFenetre()
    sys.exit(app.exec_())
    ex.show()
    a.exec_()