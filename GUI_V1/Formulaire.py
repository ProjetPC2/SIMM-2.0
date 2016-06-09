"""
Dans ce fichier vous pourrez voir :
-un exemple de creation d'un widget personnalise
-l'utilisation du form layout
-l'utilisation des Qlabel
-l'utilisation des QlineEdit
-l'utilisation des QcomboBox
-l'utilisation des QDateEdit
-l'utilisation des QRadioButton
-l'utilisation des QTextEdit
"""
import sys
from PyQt5.QtWidgets import *
import Stockage
from PyQt5.QtCore import QDate

class Formulaire(QWidget):
    """Classe représentant le formulaire de saisie d'ajout d'un equipement"""

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        #Attribut qui contiendra la liste des differents widgets
        self.widgetList = list()

        #Layout formulaire contenant les differents elements
        formulaireConteneur = QFormLayout();

        #creation de la ligne pour l'id
        idLabel = QLabel("Id :", self)
        self.idEdit = QLineEdit()

        #creation de la ligne pour la categorie d'equipement
        categorieEquipementLabel = QLabel("Categorie Equipement : ", self)
        self.categorieEquipementComboBox = QComboBox()
        for equipement in Stockage.listeCategorieEquipement:
            self.categorieEquipementComboBox.addItem(equipement)
        # creation de la ligne pour la marque de l'equipement
        marqueLabel = QLabel("Marque : ", self)
        self.marquelEdit = QLineEdit()

        # creation de la ligne pour le modele de l'equipement
        modeleLabel = QLabel("Modele : ", self)
        self.modelelEdit = QLineEdit()

        # creation de la ligne pour le numero de serie de l'equipement
        numSerieLabel = QLabel("No. de serie : ", self)
        self.numSerielEdit = QLineEdit()

        # creation de la ligne pour la categorie d'equipement
        salleLabel = QLabel("Salle : ", self)
        self.salleComboBox = QComboBox()
        for salle in Stockage.listeSalle:
            self.salleComboBox.addItem(salle)
        self.salleComboBox.setEditable(True)

        # creation de la ligne pour la categorie d'equipement
        centreServiceLabel = QLabel("Centre de service : ", self)
        self.centreServiceComboBox = QComboBox()
        for centre in Stockage.listeCentreService:
            self.centreServiceComboBox.addItem(centre)
        self.centreServiceComboBox.setEditable(True)
        # creation de la partie pour la date d'acquisition
        dateAcquisitionLabel = QLabel("Date d'acquisition : ")
        self.dateAcquisitionEdit = QDateEdit()
        self.dateAcquisitionEdit.setDate(QDate.currentDate())
        # creation de la partie pour la date du dernier entretien
        dateEntretienLabel = QLabel("Date du dernier entretien : ")
        self.dateEntretienEdit = QDateEdit()
        self.dateEntretienEdit.setDate(QDate.currentDate())

        #creation de la partie pour la provenance
        provenanceLabel = QLabel("Provenance :")
        self.provenanceEdit = QLineEdit()

        #creation de la partie pour le choix de l'etat de service
        etatServiceConteneur = QHBoxLayout()
        etatServiceLabel = QLabel("Etat de service : ")
        etatServiceRadioConteneur = QVBoxLayout()
        etatServiceEnService = QRadioButton("En service", self)
        etatServiceEnService.toggled.connect(self.enService)
        etatServiceEnService.setChecked(True)
        etatServiceEnMaintenance = QRadioButton("En maintenance", self)
        etatServiceEnMaintenance.toggled.connect(self.enMaintenance)
        etatServiceAuRebus = QRadioButton("Au rebus", self)
        etatServiceAuRebus.toggled.connect(self.auRebus)

        etatServiceGroup = QGroupBox()
        # etatServiceGroup.(etatServiceEnService)
        # etatServiceGroup.addButton(etatServiceEnMaintenance)
        # etatServiceGroup.addButton(etatServiceAuRebus)
        etatServiceRadioConteneur.addWidget(etatServiceEnService)
        etatServiceRadioConteneur.addWidget(etatServiceEnMaintenance)
        etatServiceRadioConteneur.addWidget(etatServiceAuRebus)
        etatServiceGroup.setLayout(etatServiceRadioConteneur)
        # etatServiceConteneur.addWidget(etatServiceLabel)
        # etatServiceConteneur.addLayout(etatServiceGroup)

        #creation de la partie pour le choix de l'etat de conservation
        etatConservationConteneur = QHBoxLayout()
        etatConservationLabel = QLabel("Etat de conservation : ")
        etatConservationRadioConteneur = QVBoxLayout()
        etatConservationQuasiNeuf = QRadioButton("Quasi neuf", self)
        etatConservationQuasiNeuf.toggled.connect(self.estQuasiNeuf)
        etatConservationQuasiNeuf.setChecked(True)
        etatConservationAcceptable = QRadioButton("Acceptable", self)
        etatConservationAcceptable.toggled.connect(self.acceptable)
        etatConservationEnFinDeVie = QRadioButton("En fin de vie", self)
        etatConservationEnFinDeVie.toggled.connect(self.enFinDeVie)
        etatConservationDesuet = QRadioButton("Desuet", self)
        etatConservationDesuet.toggled.connect(self.desuet)
        etatConservationGroup = QGroupBox()
        # etatConservationGroup.addButton(etatConservationQuasiNeuf)
        # etatConservationGroup.addButton(etatConservationAcceptable)
        # etatConservationGroup.addButton(etatConservationEnFinDeVie)
        # etatConservationGroup.addButton(etatConservationDesuet)
        etatConservationRadioConteneur.addWidget(etatConservationQuasiNeuf)
        etatConservationRadioConteneur.addWidget(etatConservationAcceptable)
        etatConservationRadioConteneur.addWidget(etatConservationEnFinDeVie)
        etatConservationRadioConteneur.addWidget(etatConservationDesuet)

        etatConservationGroup.setLayout(etatConservationRadioConteneur)
        radioChoice = QHBoxLayout()
        radioChoice.addWidget(etatServiceLabel)
        radioChoice.addWidget(etatServiceGroup)
        radioChoice.addWidget(etatConservationLabel)
        radioChoice.addWidget(etatConservationGroup)
        #Creation de la partie self.commentaire
        self.commentaire = QTextEdit()

        #insertion des differents elements dans le formulaireLayout
        # formulaireConteneur.insertRow(1, idLabel, self.idEdit)
        formulaireConteneur.insertRow(1, idLabel)
        formulaireConteneur.insertRow(2, categorieEquipementLabel, self.categorieEquipementComboBox)
        formulaireConteneur.insertRow(3, marqueLabel, self.marquelEdit)
        formulaireConteneur.insertRow(4, modeleLabel, self.modelelEdit)
        formulaireConteneur.insertRow(5, numSerieLabel, self.numSerielEdit)
        formulaireConteneur.insertRow(6, salleLabel, self.salleComboBox)
        formulaireConteneur.insertRow(7, centreServiceLabel, self.centreServiceComboBox)
        formulaireConteneur.insertRow(8, dateAcquisitionLabel, self.dateAcquisitionEdit)
        formulaireConteneur.insertRow(9, dateEntretienLabel, self.dateEntretienEdit)
        formulaireConteneur.insertRow(10, provenanceLabel, self.provenanceEdit)
        # formulaireConteneur.insertRow(11, etatServiceLabel, etatServiceGroup)
        # formulaireConteneur.insertRow(12, etatConservationLabel, etatConservationGroup)
        formulaireConteneur.insertRow(11, radioChoice)
        formulaireConteneur.insertRow(13, "Commentaires : ", self.commentaire)

        #insertion des differents widgets dans la liste de widgets
        self.widgetList.append(self.idEdit)
        self.widgetList.append(self.categorieEquipementComboBox)
        self.widgetList.append(self.marquelEdit)
        self.widgetList.append(self.modelelEdit)
        self.widgetList.append(self.numSerielEdit)
        self.widgetList.append(self.salleComboBox)
        self.widgetList.append(self.centreServiceComboBox)
        self.widgetList.append(self.dateAcquisitionEdit)
        self.widgetList.append(self.dateEntretienEdit)
        self.widgetList.append(self.provenanceEdit)
        self.widgetList.append(etatServiceGroup)
        self.widgetList.append(etatConservationGroup)
        self.widgetList.append(self.commentaire)

        #Layouts
        vbox = QVBoxLayout()
        vbox.addLayout(formulaireConteneur)

        # Création des variables de stockages des informatios pour les radio boutons
        self.etatService = "En service"
        self.etatConservation = "Quasi neuf"

        # Affichage de l'interface
        self.setLayout(vbox)

    def enService(self):
        self.etatService = "En service"

    def enMaintenance(self):
        self.etatService = "En maintenance"

    def auRebus(self):
        self.etatService = "Au rebus"

    def estQuasiNeuf(self,):
        self.etatConservation = "Quasi neuf"

    def acceptable(self):
        self.etatConservation = "Acceptable"

    def enFinDeVie(self):
        self.etatConservation = "En fin de vie"

    def desuet(self):
        self.etatConservation = "Desuet"


if __name__ == "__main__":

    app = QApplication(sys.argv)

    win = Formulaire()
    win.setWindowTitle("Options")
    win.show()

    sys.exit(app.exec_())