"""
Fichier de création d'une fenêtre de recherche d'un équipement :
"""
import sys

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import*

from PyQt5.QtGui import QIcon, QFont

class rechercheEquipement(QWidget):

    class listeDefilante():

        global listeCategorieEquip
        listeCategorieEquip = ["Categorie1", "Categorie2", "Categorie3"]
        global listeEtatService
        listeEtatService = ["En service", "En maintenance", "Au rebus"]
        global listeCentreService
        listeCentreService = ["Centre 1", "Centre 2", "Centre 3"]
        global listeSalle
        listeSalle = ["Chambre patient", "Salle d'operation", "Salle de reunion"]
        global listeProvenance
        listeProvenance = ["CHU Ste-Justine", "Provenance 2", "Provenance 3"]

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.widgetList = list()

        self.Titre = QLabel('Assistant de recherche - Équipement')
        self.Titre.setFont((QFont('SansSerif', 24)))

        NoSerieLabel = QLabel('Numéro de série')
        NoSerieEdit = QLineEdit()

        CategorieEquipLabel = QLabel('Catégorie d''équipement')
        CategorieEquipEdit = QLineEdit()
        CategorieEquipComboBox = QComboBox()
        for equipement in listeDefilante.listeCategorieEquip:
            CategorieEquipComboBox.addItem(equipement)

        EtatServiceLabel = QLabel('État de service')
        EtatServiceEdit = QLineEdit()
        EtatServiceComboBox = QComboBox()
        for etat in listeDefilante.listeEtatService:
            EtatServiceComboBox.addItem(etat)

        CentreServiceLabel = QLabel('Centre de service')
        CentreServiceEdit = QLineEdit()
        CentreServiceComboBox = QComboBox()
        for centre in listeDefilante.listeCentreService:
            CentreServiceComboBox.addItem(centre)

        SalleLabel = QLabel('Salle')
        SalleEdit = QLineEdit()
        SalleComboBox = QComboBox()
        for salle in listeDefilante.listeSalle:
            SalleComboBox.addItem(salle)

        ProvenanceLabel = QLabel('Provenance')
        ProvenanceEdit = QLineEdit()
        ProvenanceComboBox = QComboBox()
        for provenance in listeDefilante.listeProvenance:
            ProvenanceComboBox.addItem(provenance)


        quitButton = QPushButton("Quitter")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(quitButton)
        quitButton.clicked.connect(QCoreApplication.instance().quit)
        vbox = QVBoxLayout()
        vbox.addStretch(1)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.Titre, 1, 0)

        grid.addWidget(CategorieEquipLabel, 2, 0)
        grid.addWidget(CategorieEquipEdit, 3, 0)

        grid.addWidget(NoSerieLabel, 2, 3)
        grid.addWidget(NoSerieEdit, 3, 3)

        grid.addWidget(EtatServiceLabel, 4, 0)
        grid.addWidget(EtatServiceEdit, 5, 0)

        grid.addWidget(CentreServiceLabel, 4, 1)
        grid.addWidget(CentreServiceEdit, 5, 1)

        grid.addWidget(SalleLabel, 4, 2)
        grid.addWidget(SalleEdit, 5, 2)

        grid.addWidget(ProvenanceLabel, 4, 3)
        grid.addWidget(ProvenanceEdit, 5, 3)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

        def keyPressEvent(self, e):

            if e.key() == Qt.Key_Escape:
                self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = rechercheEquipement()
    sys.exit(app.exec_())