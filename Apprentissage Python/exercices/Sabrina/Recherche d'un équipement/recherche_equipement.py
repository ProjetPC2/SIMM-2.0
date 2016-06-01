"""
Fichier de création d'une fenêtre de recherche d'un équipement :
"""
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import *
from qtconsole.qt import QtCore
from PyQt5.QtGui import QIcon, QFont

class ListeDefilante():
    #On ne peut pas creer deux classes l'une dans l'autre
    listeCategorieEquip = ["Categorie1", "Categorie2", "Categorie3"]
    listeEtatService = ["En service", "En maintenance", "Au rebus"]
    listeCentreService = ["Centre 1", "Centre 2", "Centre 3"]
    listeSalle = ["Chambre patient", "Salle d'operation", "Salle de reunion"]
    listeProvenance = ["CHU Ste-Justine", "Provenance 2", "Provenance 3"]


class rechercheEquipement(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.widgetList = list()

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
        grid.addWidget(quitButton, 9, 1)
        quitButton.clicked.connect(QCoreApplication.instance().quit)


        self.setLayout(grid)

        self.setGeometry(300, 300, 700, 300)
        self.setWindowTitle('Projet PC2')
        self.show()

        def keyPressEvent(self, e):

            if e.key() == Qt.Key_Escape:
                self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = rechercheEquipement()
    sys.exit(app.exec_())