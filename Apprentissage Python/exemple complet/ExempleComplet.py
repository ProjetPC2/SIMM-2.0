"""
Creation de la premiere fenetre
Dans cette exemple vous pourrez voir comment :
-Créer une fenêtre
-Modifier quelques attributs de la fenêtre
-Créer un bouton
-Assigner une action à un bouton
-Mettre en place des bulles d'aide
"""

import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication, QMessageBox, QDesktopWidget, QAction, qApp, QMainWindow)
from PyQt5.QtGui import QIcon, QFont


class Fenetre(QMainWindow):
    """Classe qui nous servira d'exemple
    Notre classe hérite de la classe Qwidget"""
    def __init__(self):
        super().__init__() #appel au constructeur de la classe mère
        #creation de la fenetre graphique
        self.initUI()


    def initUI(self):
        """On definit une methode pour definir la fenetre graphique"""

        self.statusBar().showMessage('Ready')

        exitAction = QAction(QIcon('PC2.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+A')
        exitAction.setStatusTip("Quitter l'application")
        exitAction.triggered.connect(qApp.quit)

        #Creation du menu
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        # exitAction1 = QAction(QIcon('exit24.png'), 'Exit', self)
        # exitAction1.setShortcut('Ctrl+Q')
        # exitAction1.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        #On definit la police et la taille du texte dans les bulles d'aide
        QToolTip.setFont(QFont('SansSerif', 10))
        #On definit le texte a afficher lors du passage sur la fenetre
        self.setToolTip("Exemple de creation d'une <b>bulle</b> d'aide pour la fenetre")
        #Creation d'un bouton
        btn = QPushButton('Bouton', self)
        #On met en place une bulle d'aide
        btn.setToolTip("Voici un bouton inutile !")
        #On redefinit la taille sur le texte, ici on applique une taille recommandée
        btn.resize(btn.sizeHint())
        btn.move(100, 75)

        #Creation du bouton pour quitter la fenetre
        qbtn = QPushButton('Quitter', self)
        #On connecte une action au clique
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        #On met en place une bulle d'aide
        btn.setToolTip("Ce bouton sert à quitter la fenetre !")
        qbtn.resize(qbtn.sizeHint())
        #Positionnement du bouton
        qbtn.move(150, 150)


        #Definition des attributs de la fenetre
        self.resize(500,300)
        self.setWindowTitle('PC2')
        self.setWindowIcon(QIcon('PC2.png'))

    def closeEvent(self, event):
        """Fonction gerant la creation d'une fenetre de verification
        lors de la fermeture de la fenetre"""
        reply = QMessageBox.question(self, 'Message',
            "Etes-vous sur de vouloir quitter ?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        """Methode permettant de centrer la fenetre"""
        #Nous recuperons la geometrie de la fenetre principale
        qr = self.frameGeometry()
        #Nous recuperons la definition de l'ecran et nous recuperons le point central
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Fenetre()
    ex.show()
    sys.exit(app.exec_())