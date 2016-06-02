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
from PyQt5.QtCore import Qt
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
        idEdit = QLineEdit()
        #creation de la ligne pour la categorie d'equipement
        categorieEquipementLabel = QLabel("Categorie Equipement : ", self)
        categorieEquipementComboBox = QComboBox()
        for equipement in Stockage.listeCategorieEquipement:
            categorieEquipementComboBox.addItem(equipement)
        # creation de la ligne pour la marque de l'equipement
        marqueLabel = QLabel("Marque : ", self)
        marquelEdit = QLineEdit()

        # creation de la ligne pour le modele de l'equipement
        modeleLabel = QLabel("Modele : ", self)
        modelelEdit = QLineEdit()

        # creation de la ligne pour le numero de serie de l'equipement
        numSerieLabel = QLabel("No. de serie : ", self)
        numSerielEdit = QLineEdit()

        # creation de la ligne pour la categorie d'equipement
        salleLabel = QLabel("Salle : ", self)
        salleComboBox = QComboBox()
        for salle in Stockage.listeSalle:
            salleComboBox.addItem(salle)
        # creation de la ligne pour la categorie d'equipement
        centreServiceLabel = QLabel("Centre de service : ", self)
        centreServiceComboBox = QComboBox()
        for centre in Stockage.listeCentreService:
            centreServiceComboBox.addItem(centre)

        # creation de la partie pour la date d'acquisition
        dateAcquisitionLabel = QLabel("Date d'acquisition : ")
        dateAcquisitionEdit = QDateEdit()
        dateAcquisitionEdit.setDate(QDate.currentDate())
        # creation de la partie pour la date du dernier entretien
        dateEntretienLabel = QLabel("Date du dernier entretien : ")
        dateEntretienEdit = QDateEdit()
        dateEntretienEdit.setDate(QDate.currentDate())

        #creation de la partie pour la provenance
        provenanceLabel = QLabel()
        provenanceEdit = QLineEdit()

        #creation de la partie pour le choix de l'etat de service
        etatServiceConteneur = QHBoxLayout()
        etatServiceLabel = QLabel("Etat de service : ")
        etatServiceRadioConteneur = QVBoxLayout()
        etatServiceEnService = QRadioButton("En service", self)
        etatServiceEnService.toggled.connect(self.service)
        etatServiceEnService.setChecked(True)
        etatServiceEnMaintenance = QRadioButton("En maintenance", self)
        etatServiceEnMaintenance.toggled.connect(self.service)
        etatServiceAuRebus = QRadioButton("Au rebus", self)
        etatServiceAuRebus.toggled.connect(self.service)

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
        etatConservationQuasiNeuf.toggled.connect(self.conservation)
        etatConservationQuasiNeuf.setChecked(True)
        etatConservationAcceptable = QRadioButton("Acceptable", self)
        etatConservationAcceptable.toggled.connect(self.conservation)
        etatConservationEnFinDeVie = QRadioButton("En fin de vie", self)
        etatConservationEnFinDeVie.toggled.connect(self.conservation)
        etatConservationDesuet = QRadioButton("Desuet", self)
        etatConservationDesuet.toggled.connect(self.conservation)
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

        #Creation de la partie commentaire
        commentaire = QTextEdit()

        #insertion des differents elements dans le formulaireLayout
        formulaireConteneur.insertRow(1, idLabel, idEdit)
        formulaireConteneur.insertRow(2, categorieEquipementLabel, categorieEquipementComboBox)
        formulaireConteneur.insertRow(3, marqueLabel, marquelEdit)
        formulaireConteneur.insertRow(4, modeleLabel, modelelEdit)
        formulaireConteneur.insertRow(5, numSerieLabel, numSerielEdit)
        formulaireConteneur.insertRow(6, salleLabel, salleComboBox)
        formulaireConteneur.insertRow(7, centreServiceLabel, centreServiceComboBox)
        formulaireConteneur.insertRow(8, dateAcquisitionLabel, dateAcquisitionEdit)
        formulaireConteneur.insertRow(9, dateEntretienLabel, dateEntretienEdit)
        formulaireConteneur.insertRow(10, provenanceLabel, provenanceEdit)
        formulaireConteneur.insertRow(11, etatServiceLabel, etatServiceGroup)
        formulaireConteneur.insertRow(12, etatConservationLabel, etatConservationGroup)
        formulaireConteneur.insertRow(13, "Commentaires : ", commentaire)

        #insertion des differents widgets dans la liste de widgets
        self.widgetList.append(idEdit)
        self.widgetList.append(categorieEquipementComboBox)
        self.widgetList.append(marquelEdit)
        self.widgetList.append(modelelEdit)
        self.widgetList.append(numSerielEdit)
        self.widgetList.append(salleComboBox)
        self.widgetList.append(centreServiceComboBox)
        self.widgetList.append(dateAcquisitionEdit)
        self.widgetList.append(dateEntretienEdit)
        self.widgetList.append(provenanceEdit)
        self.widgetList.append(etatServiceGroup)
        self.widgetList.append(etatConservationGroup)
        self.widgetList.append(commentaire)

        #Layouts
        vbox = QVBoxLayout()
        vbox.addLayout(formulaireConteneur)

        # Création des variables de stockages des informatios pour les radio boutons
        self.etatService = ""
        self.etatConservation = ""

        # Affichage de l'interface
        self.setLayout(vbox)

    def service(self, text):
        print("service")
        self.etatService = str(text)

    def conservation(self, text):
        print("conservation")
        self.etatConservation = str(text)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    win = Formulaire()
    win.setWindowTitle("Options")
    win.show()

    sys.exit(app.exec_())