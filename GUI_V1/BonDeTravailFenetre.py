import sys

from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import*
from qtconsole.qt import QtCore
from qtpy import QtGui

from Stockage import BonDeTravail


class BonDeTravailFenetre(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.initUI()
        self.bonDeTravail = BonDeTravail()


    def initUI(self):
        # Label
        self.Titre = QLabel('Bon de travail- maintenance et réparation')
        self.Titre.setFont((QFont('SansSerif', 24)))


        ID = QLabel('ID')
        CategorieEquip = QLabel('Catégorie d''équipement')
        Marque = QLabel('Marque')
        Modele = QLabel('Modèle')
        Salle = QLabel ('Salle')
        CentreService = QLabel('Centre de service')

        Bdt = QLabel('#Bon de travail')
        Date = QLabel('Date')
        Temps = QLabel ('Temps estimé (h:m)')

        DescSit = QLabel('Description de la situation')
        DescInv = QLabel('Description de l''intervention')

        # Edit (ligne pour écrire)


        self.idEdit = QLineEdit()
        self.categorieEdit = QLabel("ici categorie")
        self.markEdit = QLabel("ici marque")
        self.modelEdit = QLabel("ici modele")
        self.salleEdit = QLabel("ici salle")
        self.centreEdit = QLabel("ici centre")

        self.bdtEdit = QLineEdit()
        self.tempsEdit = QLineEdit()

        self.descsitEdit = QTextEdit()
        self.descinvEdit = QTextEdit()


        self.okButton = QPushButton("OK")
        self.quitButton = QPushButton("Quitter")


        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.quitButton)
        self.quitButton.clicked.connect(self.quitter)
        vbox = QVBoxLayout()
        vbox.addStretch(1)

        # Partie du haut widget
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.Titre,1,0)

        grid.addWidget(ID, 2, 0)
        grid.addWidget(self.idEdit, 3, 0)

        grid.addWidget(CategorieEquip, 2, 1)
        grid.addWidget(self.categorieEdit, 3, 1)

        grid.addWidget(Marque, 4, 0)
        grid.addWidget(self.markEdit, 5, 0)

        grid.addWidget(Modele, 4, 1)
        grid.addWidget(self.modelEdit, 5, 1)

        grid.addWidget(Salle, 6, 0)
        grid.addWidget(self.salleEdit, 7, 0)

        grid.addWidget(CentreService, 6, 1)
        grid.addWidget(self.centreEdit, 7, 1)

        # Partie du bas widget
        grid2 = QGridLayout()
        grid2.setSpacing(10)

        grid2.addWidget(Bdt, 1, 0)
        grid2.addWidget(self.bdtEdit, 2, 0)

        grid2.addWidget(Date, 3, 0)
       # self.dateEdit est plus bas

        grid2.addWidget(Temps, 5, 0)
        grid2.addWidget(self.tempsEdit,6, 0)

        grid2.addWidget(DescSit, 1, 3)
        grid2.addWidget(self.descsitEdit,2, 3)

        grid2.addWidget(DescInv, 6, 3)
        grid2.addWidget(self.descinvEdit,7, 3)


    # Ouvert ou fermé
        self.combo = QComboBox(self)
        self.combo.addItem("Ouvert")
        self.combo.addItem("Fermé")

        grid2.addWidget(self.combo, 8, 3)
        self.label = QLabel("Ouvert", self)
        grid2.addWidget(self.label, 9,3)
        self.combo.activated[str].connect(self.onActivated)

        vbox.addLayout(grid)
        vbox.addLayout(grid2)
        vbox.addLayout(hbox)

        self.setLayout(vbox)



    # Fenêtre

        self.setGeometry(300, 300, 700, 600)
        self.setWindowTitle('PC2')
        self.setWindowIcon(QIcon('Images/PC2_logo.png'))
        self.show()



    # Bouton


        self.ajoutBdT = QPushButton('')
        self.ajoutBdT.setIcon(QtGui.QIcon("Images/Bouton_Sauvegarde.gif"))
        self.ajoutBdT.setIconSize(QtCore.QSize(50, 50))
        self.ajoutBdT.clicked.connect(self.enregistrer)
        grid.addWidget(self.ajoutBdT,9, 2)

        btnGG = QPushButton('<<', self)
        btnGG.resize(btnGG.sizeHint())
        grid.addWidget(btnGG, 9, 3)


        btnG = QPushButton('<', self)
        btnG.resize(btnG.sizeHint())
        grid.addWidget(btnG, 9, 4)

        btnD = QPushButton('>', self)
        btnD.resize(btnD.sizeHint())
        grid.addWidget(btnD, 9, 5)

        btnDD = QPushButton('>>', self)
        btnDD.resize(btnDD.sizeHint())
        grid.addWidget(btnDD, 9, 6)


     # Ecriture de la date sur la ligne

        self.dateEdit = QDateEdit()
        grid2.addWidget(self.dateEdit, 4, 0)
        self.dateEdit.setDate(QDate.currentDate())

    #connection

        # self.ajoutBdT.clicked.connect(self.afficheMessage)

    def onActivated(self, text):

        self.label.setText(text)
        self.label.adjustSize()
        print(text)

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()

    def quitter(self):
        # reply = QMessageBox.question(self, 'Message',
        #                              "Etes-vous sur de vouloir quitter ?", QMessageBox.Yes |
        #                              QMessageBox.No, QMessageBox.No)
        # if reply == QMessageBox.Yes:
        #     # self.hide()
        #     # self.close()
        self.destroy()

    def enregistrer(self):
        # self.categorieEdit =
        self.bonDeTravail.modifierDescriptionSituation(self.descsitEdit.toPlainText())
        self.bonDeTravail.modifierDate(self.dateEdit.date().toPyDate())
        self.bonDeTravail.modifierTempsEstime(self.tempsEdit.text())
        self.bonDeTravail.modifierDescriptionInventaire(self.descinvEdit.toPlainText())
        self.bonDeTravail.modifierEtat(self.combo.currentText())
        print(self.bonDeTravail.dictionnaire)

    def chargerEquipement(self, idEquipement):
        #equipement = chargerEquipement(idEquipement)
        equipement = dict()
        listBonDeTravail = list()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = BonDeTravailFenetre()
    sys.exit(app.exec_())