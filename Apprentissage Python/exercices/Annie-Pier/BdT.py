import sys
import random


from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import*

from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, Qt


from qtconsole.qt import QtCore
from qtpy import QtGui
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


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


        idEdit = QLineEdit()
        catEdit = QLineEdit()
        markEdit = QLineEdit()
        modelEdit = QLineEdit()
        salleEdit = QLineEdit()
        centreEdit = QLineEdit()

        bdtEdit = QLineEdit()
        tempsEdit = QLineEdit()

        descsitEdit = QTextEdit()
        descinvEdit = QTextEdit()


        okButton = QPushButton("OK")
        quitButton = QPushButton("Quitter")


        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(quitButton)
        quitButton.clicked.connect(QCoreApplication.instance().quit)
        vbox = QVBoxLayout()
        vbox.addStretch(1)

        # Partie du haut widget
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.Titre,1,0)

        grid.addWidget(ID, 2, 0)
        grid.addWidget(idEdit, 3, 0)

        grid.addWidget(CategorieEquip, 2, 1)
        grid.addWidget(catEdit, 3, 1)

        grid.addWidget(Marque, 4, 0)
        grid.addWidget(markEdit, 5, 0)

        grid.addWidget(Modele, 4, 1)
        grid.addWidget(modelEdit, 5, 1)

        grid.addWidget(Salle, 6, 0)
        grid.addWidget(salleEdit, 7, 0)

        grid.addWidget(CentreService, 6, 1)
        grid.addWidget(centreEdit, 7, 1)

        # Partie du bas widget
        grid2 = QGridLayout()
        grid2.setSpacing(10)

        grid2.addWidget(Bdt, 1, 0)
        grid2.addWidget(bdtEdit, 2, 0)

        grid2.addWidget(Date, 3, 0)
       # dateEdit est plus bas

        grid2.addWidget(Temps, 5, 0)
        grid2.addWidget(tempsEdit,6, 0)

        grid2.addWidget(DescSit, 1, 3)
        grid2.addWidget(descsitEdit,2, 3)

        grid2.addWidget(DescInv, 6, 3)
        grid2.addWidget(descinvEdit,7, 3)


    # Ouvert ou fermé
        combo = QComboBox(self)
        combo.addItem("Ouvert")
        combo.addItem("Fermé")

        grid2.addWidget(combo, 8, 3)
        self.label = QLabel("Ouvert", self)
        grid2.addWidget(self.label, 9,3)
        combo.activated[str].connect(self.onActivated)

        vbox.addLayout(grid)
        vbox.addLayout(grid2)
        vbox.addLayout(hbox)

        self.setLayout(vbox)



    # Fenêtre

        self.setGeometry(300, 300, 700, 600)
        self.setWindowTitle('PC2')
        self.setWindowIcon(QIcon('PC2_logo.png'))
        self.show()



    # Bouton


        self.ajoutBdT = QPushButton('')
        self.ajoutBdT.setIcon(QtGui.QIcon("Bouton_Sauvegarde.gif"))
        self.ajoutBdT.setIconSize(QtCore.QSize(50, 50))
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

        dateEdit = QDateEdit()
        grid2.addWidget(dateEdit, 4, 0)
        dateEdit.setDate(QDate.currentDate())

    #connection

        self.ajoutBdT.clicked.connect(self.afficheMessage)

    def onActivated(self, text):

        self.label.setText(text)
        self.label.adjustSize()
        print(text)

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()

    def keyPressEvent1(self, e):
        if e.key() == Qt.Key_Enter:
            self.setWindowTitle()

    def afficheMessage(self, event):

        """Methode affichant une fenetre de confirmation pour l'ajout d'un equipement
        Cette fenetre va nous faire passer dans le mode consultable
        Les champs ne seront plus modifiables"""
        message = QMessageBox()
        #On met le texte en gras avec les bases <b> </b>
        message.setText("<b>Sauvegarde du bon de travail</b>")
        message.setInformativeText("Vous allez sauvegarder un nouveau bon de travail")
        message.setWindowTitle("Confirmation")
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.buttonClicked.connect(self.confirmation)
        message.exec()

    def confirmation(self,i):
        #Methode qui va faire appel a la methode valider
        #Cette methode est appelee une fois que l'ajout d'un element a ete confirme
        if i.text() == "OK":
            self.valider()

    def valider(self):
        """Methode valider qui va changer le contenu de la fenetre une fois l'equipement valider
        Cette methode va tout d'abord declancher une fenetre de confirmation
        Puis si la confirmation est valide, elle va mettre les informations sous forme de Qlabel
        Les informations ne seront donc plus modifiables, on passe en mode consultatble"""
        self.formulaire.hide()
        self.validerBouton.hide()
        self.formulaireRempli.show()
        self.modifierBouton.show()
        self.statusBar().showMessage("Modification d'un equipement")
        self.donnees()
        self.resize(1000,1000)




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())