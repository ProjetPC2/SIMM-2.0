



import sys

from PyQt5.QtCore import QDate
from PyQt5 import QtGui

import Accueil
import Stockage
import Formulaire
import consultationModificationEquipementWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
class MainWindow(QMainWindow):
    """La classe MainWindow est la classe qui est va servir a creer la fenetre principale
    Cette classe va contenir les attributs suivants :
    -Un titre
    -Une statusBar
    -un formulaire
    -un formulaire rempli
    -des options
    -un attribut de stockage
    -une liste temporaire pour le stockage des informations"""
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        # Création des differents éléments
        self.formulaire = Formulaire.Formulaire(self)



if __name__ == "__main__": #Si le fichier est lancé tout seul

    app = QApplication(sys.argv)
    window = MainWindow()
    #window.center()
    window.show()
    sys.exit(app.exec_())