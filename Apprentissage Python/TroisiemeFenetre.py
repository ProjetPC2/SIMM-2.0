"""
Dans cette exemple vous pourrez voir comment :
-Creation de labels (champs de texte)
-Creation de champs de saisie de texte
-Creation de liste deroulante
-Conenxion d'evenement et mise a jour de texte
-exemple d'utilisation des layouts pour gerer le placemenet

"""

import sys

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox)


class Example(QWidget):
    """"Creation de la classe qui va gerer la fenetre
    creation des methodes evenements"""
    def __init__(self):
        #constructeur
        super().__init__()
        self.initUI()

    def initUI(self):
        #creation des labels
        nom = QLabel('Nom')
        prenom = QLabel('Prenom')
        commentaire = QLabel('Commentaire')
        #creation des champs d'entree de texte
        nomEdit = QLineEdit()
        prenomEdit = QLineEdit()
        #creation d'un champ d'entree multiligne
        commentaireEdit = QTextEdit()
        #creation des boutons
        okButton = QPushButton("OK")
        quitButton = QPushButton("Quitter")

        #creation d'un layout horizontal
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        #ajout des widget dans le layout
        hbox.addWidget(okButton)
        hbox.addWidget(quitButton)

        #connexion du l'action de fermeture de la fenetre
        quitButton.clicked.connect(QCoreApplication.instance().quit)

        #creation d'un layout verticale
        vbox = QVBoxLayout()
        vbox.addStretch(1)

        #creation d'une grid layout
        grid = QGridLayout()
        grid.setSpacing(10)

        #Postionnement des differents elements dans le grid layout
        grid.addWidget(nom, 1, 0)
        grid.addWidget(nomEdit, 1, 1)

        grid.addWidget(prenom, 2, 0)
        grid.addWidget(prenomEdit, 2, 1)

        grid.addWidget(commentaire, 3, 0)
        grid.addWidget(commentaireEdit, 3, 1, 5, 1)

        #Creation de la liste deroulante
        combo = QComboBox(self)
        #On ajoute les differents elements pour la liste deroulante
        combo.addItem("Stylo")
        combo.addItem("Feutre")
        combo.addItem("Craie")
        combo.addItem("Chocolat")
        combo.addItem("Panda")
        #ajout de la liste deroulante dans la grid layout
        grid.addWidget(combo, 8, 0)
        #creation du label qui sera mise a jour lors de la selection de la liste deroulante
        self.label = QLabel("Stylo", self)
        #ajout du label dans la grille
        grid.addWidget(self.label, 8,1)
        #On connecte la mise a jour du texte a la selection de la liste
        combo.activated[str].connect(self.onActivated)

        #On ajoute la grid layout et le layout horizontal dans le layout vertical
        vbox.addLayout(grid)
        vbox.addLayout(hbox)
        #on met en place le layout
        self.setLayout(vbox)
        #mise a jour des fenetres
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('PC2')
        self.show()

    def onActivated(self, text):
        #methode qui fera la mise a jour du label a la selection dans la liste
        self.label.setText(text)
        self.label.adjustSize()
        print(text)

    def keyPressEvent(self, e):
        #methode qui surcharge l'appuie d'une touche du clavier
        if e.key() == Qt.Key_Escape:
            #on ferme la fenetre lors de l'appuie du bouton Esc
            self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())