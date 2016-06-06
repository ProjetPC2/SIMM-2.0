# Fenetre panneau de controle du logiciel SIMM 2.0




#importation pour une fenetre simple
import sys
import AjoutEquipement
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon , QColor, QFont, QPainter, QPen
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QCoreApplication
from qtconsole.qt import QtCore

class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        #les boutons
        AddEq_Btn= QPushButton('Ajouter un \néquipement', self)
        AddEq_Btn.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        AddEq_Btn.move(75,150)
        AddEq_Btn.resize(150,100)
        AddEq_Btn.setIcon(QIcon('PdC-Bouton_Ajouter.png'))
        AddEq_Btn.setIconSize(QtCore.QSize(40, 40))

        AddEq_Btn.clicked.connect(self.AddEqForm)


        AddBTD_Btn = QPushButton('Ajouter un \nbon de travail', self)
        AddBTD_Btn.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        AddBTD_Btn.move(250,150)
        AddBTD_Btn.resize(150, 100)
        AddBTD_Btn.setIcon(QIcon('PdC_Bouton_BdT2.png'))
        AddBTD_Btn.setIconSize(QtCore.QSize(40, 40))

        ConsulterEq_Btn = QPushButton('Consulter ou \nmodifier \nun équipement', self)
        ConsulterEq_Btn.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        ConsulterEq_Btn.move(75, 300)
        ConsulterEq_Btn.resize(150,100)
        ConsulterEq_Btn.setIcon(QIcon('PdC-crayon.png'))
        ConsulterEq_Btn.setIconSize(QtCore.QSize(40, 40))

        SeachEq_Btn = QPushButton('Rechercher un \néquipement', self)
        SeachEq_Btn.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        SeachEq_Btn.move(250, 300)
        SeachEq_Btn.resize(150,100)
        SeachEq_Btn.setIcon(QIcon('PdC_Bouton_Rechercher2.png'))
        SeachEq_Btn.setIconSize(QtCore.QSize(40,40))

        SeachBDT_Btn = QPushButton('Rechercher un\nbon de travail', self)
        SeachBDT_Btn.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        SeachBDT_Btn.move(75, 450)
        SeachBDT_Btn.resize(150, 100)
        SeachBDT_Btn.setIcon(QIcon('PdC-Bouton_Recherche_BdT.png'))
        SeachBDT_Btn.setIconSize(QtCore.QSize(40,40))

        Stats_Btn = QPushButton('Voir les \nstatistiques', self)
        Stats_Btn.setFont(QFont('SansSerif', 8, QFont.Bold))
        Stats_Btn.move(250, 450)
        Stats_Btn.resize(150, 100)
        Stats_Btn.setIcon(QIcon('PdC-Bouton-stats.png'))
        Stats_Btn.setIconSize(QtCore.QSize(40,40))



        SupportPC2_Btn = QPushButton('Support \n technique', self)
        SupportPC2_Btn.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        SupportPC2_Btn.move(480,390)
        SupportPC2_Btn.resize(150, 100)
        SupportPC2_Btn.setIcon(QIcon('PC2.png'))
        SupportPC2_Btn.setIconSize(QtCore.QSize(40,40))

        PrintInventaire_Btn = QPushButton('Imprimer l"inventaire', self)
        PrintInventaire_Btn.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        PrintInventaire_Btn.move(450, 150)
        PrintInventaire_Btn.resize(210, 70)

        #initialisation  fenetre du panneau de controle
        #Les déclaration des écritures dans la fenetre
        self.textTitre = 'S.I.M.M. 2.0 \n Hôpital Saint-Michel \n '
        self.textRemarque = '                                    S.I.M.M : Système d"Iventorisation du Matériel Médical '

        #Size of the window
        self.setGeometry(400, 175, 720, 700)
        self.setWindowTitle('SIMM 2.0 : Panneau de controle')
        self.setWindowIcon(QIcon('PC2.png'))


        #Définir la couleur de l'arriere plan de la fenêtre principale
        backG = self.palette()
        backG.setColor(self.backgroundRole(), Qt.darkBlue)
        self.setPalette(backG)
        self.show()

    #declaration du  texte principal (titre) de la fenetre
    def paintEvent(self, event):

        mainTitle = QPainter()
        mainTitle.begin(self)
        self.drawText(event, mainTitle)
        mainTitle.end()

        remarque = QPainter()
        remarque.begin(self)
        self.DessinText(event, remarque)
        remarque.end()

        ligne = QPainter()
        ligne.begin(self)
        self.drawLines(event, ligne)
        ligne.end()

    #Mise en forme du texte principal (titre) de la fenetre
    def drawText (self, event, mainTitle):
         mainTitle.setPen(QColor(Qt.white))
         mainTitle.setFont(QFont('Cambria', 24))
         mainTitle.drawText(event.rect(), Qt.AlignHCenter, self.textTitre)


    # Mise en forme du texte principal (titre) de la fenetre
    def DessinText(self, event, remarque):
        remarque.setPen(QColor(Qt.white))
        remarque.setFont(QFont('Cambria', 12 ))
        remarque.drawText(event.rect(), Qt.AlignBottom, self.textRemarque)


    def drawLines(self, event, ligne):
          pen = QPen(Qt.white, 1, Qt.SolidLine)
          ligne.setPen(pen)
          ligne.drawLine(190, 100, 540, 100)

    def AddEqForm(self):
        self.hide()
        self.AjoutEquipement.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())

