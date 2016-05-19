import sys

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        nom = QLabel('Nom')
        prenom = QLabel('Prenom')
        commentaire = QLabel('Commentaire')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
        okButton = QPushButton("OK")
        quitButton = QPushButton("Quitter")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(quitButton)
        quitButton.clicked.connect(QCoreApplication.instance().quit)
        vbox = QVBoxLayout()
        vbox.addStretch(1)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(nom, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(prenom, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(commentaire, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        combo = QComboBox(self)
        combo.addItem("Stylo")
        combo.addItem("Feutre")
        combo.addItem("Craie")
        combo.addItem("Chocolat")
        combo.addItem("Panda")
        grid.addWidget(combo, 8, 0)
        self.label = QLabel("Stylo", self)
        grid.addWidget(self.label, 8,1)
        combo.activated[str].connect(self.onActivated)

        vbox.addLayout(grid)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('PC2')
        self.show()

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