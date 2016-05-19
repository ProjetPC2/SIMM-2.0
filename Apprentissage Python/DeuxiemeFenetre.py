"""
Creation de la quatrieme fenetre
Dans cette exemple vous pourrez voir comment :
-Creer des boutons dynamiquement
"""

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication)


class Example(QWidget):
    """ Fonction creeant une fenetre
     avec des boutons a partir d'une liste"""
    def __init__(self):
        #constructeur
        super().__init__()
        self.initUI()


    def initUI(self):
        #Creation d'une grille layout
        grid = QGridLayout()
        self.setLayout(grid)
        #liste pour la creation des boutons
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        #creation d'une liste de tuple pour le positionnement des boutons
        positions = [(i,j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            #creation des boutons
            if name == '':
                continue
            #on cree le bouton
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':
    #creation de la fenetre
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())