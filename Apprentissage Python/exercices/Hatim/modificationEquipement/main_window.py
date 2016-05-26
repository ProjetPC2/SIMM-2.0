"""
Fenêtre de consultation d’un équipement et de modification d’un équipement.

Par: Hatim
Inspiré des fenêtres d'Alexandre
"""

import sys
from PyQt5 import QtGui

from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox)
from qtconsole.qt import QtCore
from qtpy import QtGui


class ConsultationModificationEquipement(QWidget):
    """"Création de la classe qui va gérer la fenetre
    création des méthodes événements"""
    def __init__(self):
        #constructeur
        super().__init__()
        self.initUI()

    def initUI(self):

        #Création des labels
        titre = QLabel("Consultation et Modification d'un Équipement")
        titre.setFont((QFont('SansSerif', 24)))
        identifiant = QLabel('ID')
        categorie = QLabel('Catégorie')
        marque = QLabel('Marque')
        modele = QLabel('Modèle')
        numeroDeSerie = QLabel('No. de série')
        salle = QLabel('Salle')
        centreDeService = QLabel('Centre de service')
        dateDacquisititon = QLabel("Date d'acquisition")
        dateDuDernierEntretien = QLabel('Date du dernier entretien')
        provenance = QLabel('Provenance')
        etatDeService = QLabel('État de service')
        listeDesBonsDeTravail = QLabel('Liste des bons de travail')
        etatDeConservation = QLabel('État de conservation')
        commentaires = QLabel('Commentaires')


        #Création des champs d'entrée de texte
        identifiantEdit = QLineEdit()
        categorieEdit = QLineEdit()
        marqueEdit = QLineEdit()
        modeleEdit = QLineEdit()
        numeroDeSerieEdit = QLineEdit()
        salleEdit = QLineEdit()
        centreDeServiceEdit = QLineEdit()
        dateDacquisititonEdit = QLineEdit()
        dateDuDernierEntretienEdit = QLineEdit()
        provenanceEdit = QLineEdit()
        etatDeServiceEdit = QLineEdit()
        listeDesBonsDeTravailEdit = QLineEdit()
        etatDeConservationEdit = QLineEdit()


        #Création d'un champ d'entrée multiligne
        commentairesEdit = QTextEdit()

        #Création des boutons
        self.nouveauBonDeTravailButton = QPushButton("Nouveau bon de travail")
        self.nouveauBonDeTravailButton.setIcon(QtGui.QIcon("Add-icon.png"))
        self.nouveauBonDeTravailButton.setIconSize(QtCore.QSize(50, 50))

        self.modifierEquipementButton = QPushButton("Modifier l'équipement")
        self.modifierEquipementButton.setIcon(QtGui.QIcon("Modify-icon.png"))
        self.modifierEquipementButton.setIconSize(QtCore.QSize(50, 50))

        self.afficherBonDeTravailButton = QPushButton("Afficher le bon de travail sélectionné")
        self.afficherBonDeTravailButton.setIcon(QtGui.QIcon("view-icon2.png"))
        self.afficherBonDeTravailButton.setIconSize(QtCore.QSize(50, 50))

        #Création d'un layout horizontal
        hbox = QHBoxLayout()
        #hbox.addStretch(1)

        # Création d'un second layout horizontal pour le titre
        hbox2 = QHBoxLayout()
        #hbox2.addStretch(1)
        hbox2.setAlignment(Qt.AlignCenter)


        #Ajout des widget dans le layout principal
        hbox.addWidget(self.nouveauBonDeTravailButton)
        hbox.addWidget(self.modifierEquipementButton)
        hbox.addWidget(self.afficherBonDeTravailButton)

        # Ajout du label du titre dans le layout horizontal 2
        hbox2.addWidget(titre)

        #Création d'un layout vertical
        vbox = QVBoxLayout()
        vbox.addStretch(1)

        #Création d'une grid layout
        grid = QGridLayout()
        grid.setSpacing(10)

        #Postionnement des differents elements dans le grid layout
        grid.addWidget(identifiant, 1, 0)
        grid.addWidget(identifiantEdit, 1, 1)

        grid.addWidget(categorie, 2, 0)
        grid.addWidget(categorieEdit, 2, 1)

        grid.addWidget(marque, 3, 0)
        grid.addWidget(marqueEdit, 3, 1)

        grid.addWidget(modele, 4, 0)
        grid.addWidget(modeleEdit, 4, 1)

        grid.addWidget(numeroDeSerie, 5, 0)
        grid.addWidget(numeroDeSerieEdit, 5, 1)

        grid.addWidget(salle, 6, 0)
        grid.addWidget(salleEdit, 6, 1)

        grid.addWidget(centreDeService, 7, 0)
        grid.addWidget(centreDeServiceEdit, 7, 1)

        grid.addWidget(dateDacquisititon, 8, 0)
        grid.addWidget(dateDacquisititonEdit, 8, 1)

        grid.addWidget(dateDuDernierEntretien, 9, 0)
        grid.addWidget(dateDuDernierEntretienEdit, 9, 1)

        grid.addWidget(provenance, 10, 0)
        grid.addWidget(provenanceEdit, 10, 1)

        grid.addWidget(etatDeService, 11, 0)
        grid.addWidget(etatDeServiceEdit, 11, 1)

        grid.addWidget(listeDesBonsDeTravail, 12, 0)
        grid.addWidget(listeDesBonsDeTravailEdit, 12, 1)

        grid.addWidget(etatDeConservation, 13, 0)
        grid.addWidget(etatDeConservationEdit, 13, 1)

        grid.addWidget(commentaires, 14, 0)
        grid.addWidget(commentairesEdit, 14, 1, 5, 1)

        # Mise en place de la forme de la fenetre
        self.setGeometry(200, 100, 200, 1000)
        self.resize(1000, 1000)
        self.setWindowTitle("SIMM 2.0")
        self.setWindowIcon(QIcon('PC2.png'))

        # Connection des differents actions au click d'un bouton
        self.nouveauBonDeTravailButton.clicked.connect(self.NouveauBonDeTravail)

        #On ajoute la grid layout et le layout horizontal dans le layout vertical
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox)
        vbox.addLayout(grid)

        #On met en place le layout
        self.setLayout(vbox)

        #Mise a jour des fenetres
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('PC2')
        self.show()

    def NouveauBonDeTravail(self, event):
        """Methode affichant une fenetre de confirmation pour l'ajout d'un bon de travail"""

        message = QMessageBox()
        message.setWindowIcon(QIcon('PC2.png'))
        # On met le texte en gras avec les bases <b> </b>
        message.setText("<b>Sauvegarde de l'equipement</b>")
        message.setInformativeText("Vous allez ajouter un nouveau bon de travail.")
        message.setWindowTitle("Confirmation")
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.buttonClicked.connect(self.confirmation)
        message.exec()

    def confirmation(self, i):
        # Methode qui va faire appel a la methode valider
        # Cette methode est appelee une fois que l'ajout d'un element à été confirmé
        if i.text() == "OK":
            self.valider()

    def valider(self):
        """Methode affichant une fenetre de confirmation pour quiter"""
        message = QMessageBox()
        message.setWindowIcon(QIcon('PC2.png'))
        # On met le texte en gras avec les bases <b> </b>
        message.setText("<b>Sauvegarde de l'equipement</b>")
        message.setInformativeText("Le formulaire de bon de travail n'est pas encore connecté!"
                                   "\nIl le sera sous peu.\nAppuyez sur OK pour quitter.")
        message.setWindowTitle("Message")
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.buttonClicked.connect(self.close)
        message.exec()


    def keyPressEvent(self, e):
        #methode qui surcharge l'appuie d'une touche du clavier
        if e.key() == Qt.Key_Escape:
            #on ferme la fenetre lors de l'appuie du bouton Esc
            self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    fenetre = ConsultationModificationEquipement()
    sys.exit(app.exec_())