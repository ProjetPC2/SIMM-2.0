# Fenetre panneau de controle du logiciel SIMM 2.0

#importation pour une fenetre simple
from AjouterEquipementFenetre import *
from ConsultationModificationEquipementFenetre import *
from RechercheBdT import RechercheBdT
from RechercherEquipementFenetre import *
from StatistiqueFenetre import *
from SupportFenetre import *


class Main(QDialog):

    def __init__(self):
        super().__init__()
        #creation des variables pour les differentes fenetres
        # self.ajouterEquipement = None
        # self.ajouterBdT = None
        # self.consulterModifierEquipement = None
        # self.rechercherEquipement = None
        # self.rechercheBdT = None
        # self.statistique = None
        self.listeBouton = list()
        self.initUI()



    def initUI(self):
        # self.ajoutEquipement = AjoutEquipement()

        #les boutons
        self.ajouterEquipementBouton= QPushButton('Ajouter un \néquipement', self)
        self.ajouterEquipementBouton.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        self.ajouterEquipementBouton.move(75,150)
        self.ajouterEquipementBouton.resize(150,100)
        self.ajouterEquipementBouton.setIcon(QIcon('Images/PdC-Bouton_Ajouter.png'))
        self.ajouterEquipementBouton.setIconSize(QtCore.QSize(40, 40))
        self.ajouterEquipementBouton.clicked.connect(self.AddEqForm)
        self.ajouterEquipementBouton.setObjectName("ajouterEquipementBouton")


        self.ajouterBonDeTravailBouton = QPushButton('Ajouter un \nbon de travail', self)
        self.ajouterBonDeTravailBouton.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        self.ajouterBonDeTravailBouton.move(250,150)
        self.ajouterBonDeTravailBouton.resize(150, 100)
        self.ajouterBonDeTravailBouton.setIcon(QIcon('Images/PdC_Bouton_BdT2.png'))
        self.ajouterBonDeTravailBouton.setIconSize(QtCore.QSize(40, 40))
        self.ajouterBonDeTravailBouton.clicked.connect(self.ouvrirFenetreAjoutBdT)
        self.ajouterBonDeTravailBouton.setObjectName("ajouterBonDeTravailBouton")


        self.consulterEquipementBouton = QPushButton('Consulter ou \nmodifier \nun équipement', self)
        self.consulterEquipementBouton.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        self.consulterEquipementBouton.move(75, 300)
        self.consulterEquipementBouton.resize(150,100)
        self.consulterEquipementBouton.setIcon(QIcon('Images/PdC-crayon.png'))
        self.consulterEquipementBouton.setIconSize(QtCore.QSize(40, 40))
        self.consulterEquipementBouton.clicked.connect(self.ouvrirFenetreConsultationEquipement)
        self.consulterEquipementBouton.setObjectName("consulterEquipementBouton")


        self.rechercheEquipementBouton = QPushButton('Rechercher un \néquipement', self)
        self.rechercheEquipementBouton.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        self.rechercheEquipementBouton.move(250, 300)
        self.rechercheEquipementBouton.resize(150,100)
        self.rechercheEquipementBouton.setIcon(QIcon('Images/PdC_Bouton_Rechercher2.png'))
        self.rechercheEquipementBouton.setIconSize(QtCore.QSize(40,40))
        self.rechercheEquipementBouton.clicked.connect(self.ouvrirFenetreRechercheEquipement)
        self.rechercheEquipementBouton.setObjectName("rechercheEquipementBouton")

        self.rechercheBonDeTravailBouton = QPushButton('Rechercher un\nbon de travail', self)
        self.rechercheBonDeTravailBouton.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        self.rechercheBonDeTravailBouton.move(75, 450)
        self.rechercheBonDeTravailBouton.setMaximumSize(300, 300)
        self.rechercheBonDeTravailBouton.setIcon(QIcon('Images/PdC-Bouton_Recherche_BdT.png'))
        self.rechercheBonDeTravailBouton.setIconSize(QtCore.QSize(40,40))
        self.rechercheBonDeTravailBouton.setObjectName("rechercheBonDeTravailBouton")
        self.rechercheBonDeTravailBouton.clicked.connect(self.ouvrirRechercheBdT)

        self.statistiqueBouton = QPushButton('Voir les \nstatistiques', self)
        self.statistiqueBouton.setFont(QFont('SansSerif', 8, QFont.Bold))
        self.statistiqueBouton.move(250, 450)
        self.statistiqueBouton.setMaximumSize(300, 300)
        self.statistiqueBouton.setIcon(QIcon('Images/PdC-Bouton-stats.png'))
        self.statistiqueBouton.setIconSize(QtCore.QSize(40,40))
        self.statistiqueBouton.clicked.connect(self.ouvrirStatistique)
        self.statistiqueBouton.setObjectName("statistiqueBouton")

        self.supportBouton = QPushButton('Support \n technique', self)
        self.supportBouton.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        self.supportBouton.move(480,390)
        self.supportBouton.setMaximumSize(300, 300)
        self.supportBouton.setIcon(QIcon('Images/PC2.png'))
        self.supportBouton.setIconSize(QtCore.QSize(150,150))
        # self.supportBouton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.supportBouton.clicked.connect(self.ouvrirFenetreSupport)
        self.supportBouton.setObjectName("supportBouton")

        self.inventaireBouton = QPushButton('Imprimer l"inventaire', self)
        self.inventaireBouton.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        self.inventaireBouton.move(450, 150)
        self.inventaireBouton.resize(210, 70)
        self.inventaireBouton.setObjectName("inventaireBouton")

        #initialisation  fenetre du panneau de controle
        #Les déclaration des écritures dans la fenetre
        self.textTitre = QLabel("S.I.M.M. 2.0 <br> <u>Hôpital Saint-Michel</u>  ")
        self.textTitre.setStyleSheet("color: white")
        self.textTitre.setFont(QFont('Cambria', 24))
        self.textTitre.setAlignment(Qt.AlignHCenter)
        self.textTitre.wordWrap()

        self.textRemarque = QLabel("S.I.M.M : Système d'Inventorisation du Matériel Médical")
        self.textRemarque.setStyleSheet("color: white")
        self.textRemarque.setFont(QFont('Cambria', 12 ))
        self.textRemarque.setAlignment(Qt.AlignBottom)
        self.textRemarque.setAlignment(Qt.AlignCenter)

        #Size of the window
        self.setGeometry(400, 175, 720, 700)
        self.setWindowTitle('SIMM 2.0 : Panneau de controle')
        self.setWindowIcon(QIcon('Images/PC2.png'))


        layoutFond = QVBoxLayout()
        layoutConteneur = QHBoxLayout()
        layoutHorizontalGauche = QVBoxLayout()
        layoutHorizontalCentre = QVBoxLayout()
        layoutHorizontalDroit = QVBoxLayout()

        layoutHorizontalGauche.addWidget(self.ajouterEquipementBouton)
        layoutHorizontalGauche.addWidget(self.consulterEquipementBouton)
        layoutHorizontalGauche.addWidget(self.rechercheBonDeTravailBouton)

        layoutHorizontalCentre.addWidget(self.ajouterBonDeTravailBouton)
        layoutHorizontalCentre.addWidget(self.rechercheEquipementBouton)
        layoutHorizontalCentre.addWidget(self.statistiqueBouton)

        layoutHorizontalDroit.addWidget(self.inventaireBouton)
        layoutHorizontalDroit.addWidget(self.supportBouton)

        layoutConteneur.addLayout(layoutHorizontalGauche)
        layoutConteneur.addLayout(layoutHorizontalCentre)
        layoutConteneur.addLayout(layoutHorizontalDroit)

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        spacerItem1 = QSpacerItem(80, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        layoutFond.addWidget(self.textTitre)
        layoutFond.addItem(spacerItem1)

        layoutFond.addLayout(layoutConteneur)
        layoutFond.addItem(spacerItem)

        layoutFond.addWidget(self.textRemarque)

        layoutFond.addItem(spacerItem)


        #Définir la couleur de l'arriere plan de la fenêtre principale
        self.setObjectName("PanneauControle")
        self.setLayout(layoutFond)
        self.setStyleSheet((open("style.qss", "r").read()))
        backG = self.palette()
        backG.setColor(self.backgroundRole(), Qt.darkBlue)
        self.setPalette(backG)
        self.setMaximumSize(1500,1000)
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
         # mainTitle.drawText(event.rect(), Qt.AlignHCenter, self.textTitre)


    # Mise en forme du texte principal (titre) de la fenetre
    def DessinText(self, event, remarque):
        remarque.setPen(QColor(Qt.white))
        remarque.setFont(QFont('Cambria', 12 ))
        # remarque.drawText(event.rect(), Qt.AlignBottom, self.textRemarque)


    def drawLines(self, event, ligne):
          pen = QPen(Qt.white, 1, Qt.SolidLine)
          ligne.setPen(pen)
          # ligne.drawLine(200,200, 600,200)
          # ligne.drawLine(190, 100, 540, 100)

    def AddEqForm(self):
        # self.hide()
        # AjoutEquipement(self).show()
        # self.ajouterEquipement = MainWindow()
        # self.ajouterEquipement.show()
        # self.listeBouton.append(MainWindow())
        # self.listeBouton[0].show()
        self.estPresent(AjouterEquipementFenetre(self))

    def ouvrirFenetreAjoutBdT(self):
        # self.ajouterBdT = BonDeTravailFenetre()
        # self.ajouterBdT.show()
        # self.ajouterEquipement.hide()
        self.estPresent(BonDeTravailFenetre(self), 1)

    def ouvrirFenetreConsultationEquipement(self):
        # self.consulterModifierEquipement = ConsultationModificationEquipement()
        # self.consulterModifierEquipement.show()
        self.estPresent(ConsultationModificationEquipement())

    def ouvrirFenetreRechercheEquipement(self):
        # self.rechercherEquipement = rechercheEquipement()
        # self.rechercherEquipement.show()
        self.estPresent(RerchercherEquipementFenetre())

    def ouvrirFenetreSupport(self):
        # self.rechercherEquipement = rechercheEquipement()
        # self.rechercherEquipement.show()
        self.estPresent(Support(self))

    def ouvrirStatistique(self):
        self.estPresent(Statistique(self))

    def ouvrirRechercheBdT(self):
        self.estPresent(RechercheBdT())

    def estPresent(self,type, fenetre = 0):
        present = False
        indice = 0
        for bouton in self.listeBouton:
            if bouton is type:
                present = True
                indice += 1
                break
            indice += 1
        if not present:
            self.listeBouton.append(type)
        self.listeBouton[indice].show()
        if fenetre == 0:
            self.listeBouton[indice].center()

    def center(self):
        """Methode permettant de centrer la fenetre"""
        # Nous recuperons la geometrie de la fenetre principale
        qr = self.frameGeometry()
        # Nous recuperons la definition de l'ecran et nous recuperons le point central
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        # self.move(qr.center)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.center()
    sys.exit(app.exec_())

