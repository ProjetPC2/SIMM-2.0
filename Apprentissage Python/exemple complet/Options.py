"""
Dans cette exemple vous pourrez voir comment :
-Creer un widget
-Voir l'utilisation des radio boutons
-voir l'utilisation des check box
-voir des exemples d'utilisations de signaux et d'actions une fois le signal attrape
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication,
                             QLabel, QCheckBox,
                             QRadioButton, QVBoxLayout)

class Options(QWidget):
    """Classe représentant les options de configuration
    Cette classe sera mise a jour pour etre integree dans un exemple"""

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # Création des éléments
        # Label
        label = QLabel("Options", self)
        label.setAlignment(Qt.AlignHCenter)
        # Radio Buttons
        restart_nowCB = QRadioButton("Redémarrer maintenant", self)
        restart_laterCB = QRadioButton("Redémarrer plus tard", self)
        restart_nowCB.toggled.connect(self.setRestart)
        restart_laterCB.toggle()
        # Check Box
        permanentCB = QCheckBox("Permanent", self)
        permanentCB.stateChanged.connect(self.setPermanent)

        # Layouts
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(restart_nowCB)
        vbox.addWidget(restart_laterCB)
        vbox.addWidget(permanentCB)


        # Création des variables
        self.permanent = False
        self.restart_now = False

        # Affichage de l'interface
        self.setLayout(vbox)

    def setPermanent(self, state):
        if state == Qt.Checked:
            self.permanent = True
        else:
            self.permanent = False

    def setRestart(self, state):
        self.restart_now = state

    def getPermanent(self):
        """Renvoie l'état du """
        return self.permanent

    def getRestart(self):
        return self.restart_now

if __name__ == "__main__":

    app = QApplication(sys.argv)

    win = Options()
    win.setWindowTitle("Options")
    win.show()

    sys.exit(app.exec_())