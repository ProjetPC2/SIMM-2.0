import sys
import random


from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import*

from PyQt5.QtCore import QDate


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # Label
        Titre = QLabel('Bon de travail- maintenance et réparation')


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

                 # Nombre aléatoire
        a= random.randrange(0, 101, 2)
        b= str(a)
        idEdit = QLineEdit(b)

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

        grid.addWidget(Titre,1,0)

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
        self.show()



    # Bouton


        btn = QPushButton('Ajout bon travail', self)
       # btn.setIcon(QIcon('fleche-gauche-droite.png'))
       # btn.setIconSize(QtCore.QSize(24,24))
        btn.resize(btn.sizeHint())
        grid.addWidget(btn,9, 6)

        btn2 = QPushButton('<', self)
        btn2.resize(btn.sizeHint())
        grid.addWidget(btn2, 9, 7)

        btn3 = QPushButton('>', self)
        btn3.resize(btn.sizeHint())
        grid.addWidget(btn3, 9, 8)


     # Ecriture de la date sur la ligne

        dateEdit = QDateEdit()
        grid2.addWidget(dateEdit, 4, 0)
        dateEdit.setDate(QDate.currentDate())

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




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())