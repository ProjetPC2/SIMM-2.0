"""
Dans cette exemple vous pourrez voir comment :
-Creer une fenetre avec differents composants
-Utiliser plusieurs classes pour faire une fenetre
-Relier des signaux a des actions
-Mettre a jour une fentre dynamiquement
-exemple d'utilisation des layouts pour gerer le placemenet
"""

import sys

from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import *

from AbstractWindow import AbstractWindow

class Statistique(QDialog, AbstractWindow):
    """La classe Statistique est la classe qui est va servir a creer la fenetre principal
    Cette classe va contenir les attributs suivants :
    -Un titre
    -Une statusBar
    -un formulaire
    -un formulaire rempli
    -des options
    -un attribut de stockage
    -une liste temporaire pour le stockage des informations"""
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        # Création des differents éléments
        self.titre = QLabel("Statistique")
        self.titre.setFont((QFont('SansSerif', 24)))
        self.titre.setAlignment(Qt.AlignCenter)

           # Création des Boutons
        self.nombreEquipement = 10
        self.labelNombreEquipement = QLabel(("Il y a <b>%d</b> equipement") %self.nombreEquipement)




        #Mise en place du layout principal
        horizontalLayout = QHBoxLayout()
        etatDeConservationLayout = QVBoxLayout()
        nombreEquipementEtatConservationLabel = QLabel("<b>Nombre d'equipement par etat de conservation</b>")
        self.nombreQuasiNeuf = 3
        self.quasiNeufLabel = QLabel("Quasi Neuf : %d" %self.nombreQuasiNeuf)

        self.nombreAcceptable = 2
        self.acceptableLabel = QLabel("Acceptable : %d" %self.nombreAcceptable)

        self.nombreEnFinVie = 2
        self.enFinVieLabel = QLabel("En fin de vie : %d" %self.nombreEnFinVie)

        self.desuet = 3
        self.desuetLabel = QLabel("Desuet : %d" %self.desuet)

        etatDeConservationLayout.addWidget(nombreEquipementEtatConservationLabel)
        etatDeConservationLayout.addWidget(self.quasiNeufLabel)
        etatDeConservationLayout.addWidget(self.acceptableLabel)
        etatDeConservationLayout.addWidget(self.enFinVieLabel)
        etatDeConservationLayout.addWidget(self.desuetLabel)


        etatDeServiceLayout = QVBoxLayout()

        nombreEquipementEtatServiceLabel = QLabel("<b>Nombre d'equipement par etat de service</b>")
        self.enService = 7
        self.enServiceLabel = QLabel("Quasi Neuf : %d" % self.enService)

        self.enMaintenance = 2
        self.enMaintenanceLabel = QLabel("Acceptable : %d" % self.enMaintenance)

        self.auRebus = 1
        self.auRebusLabel = QLabel("En fin de vie : %d" % self.auRebus)

        etatDeServiceLayout.addWidget(nombreEquipementEtatServiceLabel)
        etatDeServiceLayout.addWidget(self.enServiceLabel)
        etatDeServiceLayout.addWidget(self.enMaintenanceLabel)
        etatDeServiceLayout.addWidget(self.auRebusLabel)


        horizontalLayout.addLayout(etatDeConservationLayout)
        horizontalLayout.addLayout(etatDeServiceLayout)

        nombreEquipementProvenanceLabel = QLabel("<b>Nombre d'equipement par Provenance</b>")
        provenance = QHBoxLayout()
        provenanceLabel = QLabel("Provenance choix ")
        self.listeComboProvenance = QComboBox()
        self.listeComboProvenance.addItem("provenance1")
        self.listeComboProvenance.addItem("provenance2")
        self.listeComboProvenance.addItem("provenance3")

        provenance.addWidget(provenanceLabel)
        provenance.addWidget(self.listeComboProvenance)

        nombreEquipementProvenance = 90
        self.nombreEquipementProvenanceChoisi = QLabel("Nombre d'equipement de cette provenance : %d" %nombreEquipementProvenance)

        resume = QHBoxLayout()
        resumeLabel = QLabel("<b>Resume d'inventaire par centre de Service</b>")
        self.listeComboService = QComboBox()
        self.listeComboService.addItem("service1")
        self.listeComboService.addItem("service2")
        self.listeComboService.addItem("service3")
        resume.addWidget(resumeLabel)
        resume.addWidget(self.listeComboService)

        # donnees tests sous forme d'une liste de tuple
        tableData = [
            ("Service", '21'),
            ("Chaise", '12'),
            ("Lit", '33')
        ]

        # creation d'une table widget de taille 3x2
        self.table = QTableWidget(3, 2)
        # on met les titres des colonnes
        self.table.setHorizontalHeaderLabels(["Categorie equipement", "Quantite"])
        self.table.resize(300, 300)
        self.table.resizeRowsToContents()
        # remplissage du tableau
        for i, (name, color) in enumerate(tableData):
            # Creation des QTableWidgetItem
            nameItem = QTableWidgetItem(name)
            colorItem = QTableWidgetItem(color)
            # Insertion des elements
            self.table.setItem(i, 0, nameItem)
            self.table.setItem(i, 1, colorItem)
        self.table.resizeColumnToContents(0)
        self.table.resizeRowsToContents()
        # On fait en sorte que la table prend la largeur de la fenetre
        self.table.horizontalHeader().setStretchLastSection(True)


        # Window sera le layout vertical principal qui contiendra les autres layout
        window = QVBoxLayout()
        window.addWidget(self.titre)
        window.addWidget(self.labelNombreEquipement)
        window.addLayout(horizontalLayout)
        window.addWidget(nombreEquipementProvenanceLabel)
        window.addLayout(provenance)
        window.addWidget(self.nombreEquipementProvenanceChoisi)
        window.addLayout(resume)
        window.addWidget(self.table)
        # on normalise l'espacement des differents elements de la fenetre
        window.addStretch(1)

        #Mise en place de la forme de la fenetre
        self.setLayout(window)
        # self.setGeometry(200, 100, 200, 1000)
        self.resize(1000,1000)
        self.setWindowTitle("SIMM 2.0")
        self.setWindowIcon(QIcon('Images\PC2.png'))

    def center(self):
        """Methode permettant de centrer la fenetre"""
        # Nous recuperons la geometrie de la fenetre principale
        qr = self.frameGeometry()
        # Nous recuperons la definition de l'ecran et nous recuperons le point central
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        # self.move(qr.topLeft())
        # self.move(qr.center)

    def closeEvent(self, event):
        """Fonction gerant la creation d'une fenetre de verification
        lors de la fermeture de la fenetre"""
        reply = QMessageBox.question(self, 'Message',
                                     "Etes-vous sur de vouloir quitter ?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        #Selon le choix on fait une action precise
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def quitter(self):
        reply = QMessageBox.question(self, 'Message',
                                     "Etes-vous sur de vouloir quitter ?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # self.hide()
            # self.close()
            self.destroy()


    def valider(self):
        """Methode valider qui va changer le contenu de la fenetre une fois l'equipement valider
        Cette methode va tout d'abord declancher une fenetre de confirmation
        Puis si la confirmation est valide, elle va mettre les informations sous forme de Qlabel
        Les informations ne seront donc plus modifiables, on passe en mode consultatble"""
        self.formulaire.hide()
        self.validerBouton.hide()
        self.formulaireRempli.show()
        self.modifierBouton.show()
        self.donnees()
        self.remplissageFormulaire()
        self.listeTemp.clear()
        self.resize(1000,1000)

    def modifier(self):
        """Methode modifier permet de passer du mode consultable au mode modifiable
        Cette methode donne la possibilite a l'utilisateur de changer les differents champs
        On retourne dans le meme version que l'ajout d'un equipement"""
        self.formulaireRempli.hide()
        self.modifierBouton.hide()
        self.formulaire.show()
        self.validerBouton.show()

    def afficheMessage(self, event):
        """Methode affichant une fenetre de confirmation pour l'ajout d'un equipement
        Cette fenetre va nous faire passer dans le mode consultable
        Les champs ne seront plus modifiables"""
        message = QMessageBox()
        #On met le texte en gras avec les bases <b> </b>
        message.setText("<b>Sauvegarde de l'equipement</b>")
        message.setInformativeText("Vous allez sauvegarder un nouvel equipement")
        message.setWindowTitle("Confirmation")
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.buttonClicked.connect(self.confirmation)
        message.exec()

    def confirmation(self,i):
        #Methode qui va faire appel a la methode valider
        #Cette methode est appelee une fois que l'ajout d'un element a ete confirme
        if i.text() == "OK":
            self.valider()

    def donnees(self):
        """Methode permettant la recuperation des donnees dans les differents widgets
        On parcours la liste des widgets et on recupere les differentes informations utiles
        Les informations sont recuperees de facon specifique selon le type du widget"""
        for widget in self.formulaire.widgetList:
            # self.stockage.dictionnaire
            if type(widget) is QLineEdit:
                self.listeTemp.append(widget.text())
            elif type(widget) is QDateEdit:
                self.listeTemp.append(str(widget.date()))
                print(widget.date())
                print(QDate.currentDate())
            elif type(widget) is QComboBox:
                self.listeTemp.append(widget.currentText())
                print(widget.currentText())
            elif type(widget) is QGroupBox:
                self.listeTemp.append(self.formulaire.etatService)
            else:
                self.listeTemp.append(widget.toPlainText())
                print(widget.toPlainText())

    def remplissageFormulaire(self):
        """Methode permettant de remplir le formulaire dans le mode consultable"""
        i = 0
        for text in self.listeTemp:
            self.formulaireRempli.widgetList[i].setText(text)
            i += 1




if __name__ == "__main__": #Si le fichier est lancé tout seul

    app = QApplication(sys.argv)
    window = Statistique()
    # window.center()
    window.show()
    sys.exit(app.exec_())