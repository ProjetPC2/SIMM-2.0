# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controlPannel.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1219, 943)
        MainWindow.setStyleSheet("#MainWindow{\n"
"background: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.framePanneauDeControle = QtWidgets.QFrame(self.centralwidget)
        self.framePanneauDeControle.setStyleSheet("#framePanneauDeControle {\n"
"background: rgb(250, 250, 250);\n"
"min-width:220px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"min-width: 50px;\n"
"max-width: 150px;\n"
"}\n"
"\n"
"QDateEdit {\n"
"max-width: 105px\n"
"}\n"
"\n"
"QPushButton {\n"
"color: black;\n"
"background-color: rgb(234, 234, 234);\n"
"border-width: 2px;\n"
"border-color: grey;\n"
"border-style: solid;\n"
"border-radius: 4px;\n"
"padding: 3px;\n"
"font: bold 14px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 40px;\n"
"max-width:220px;\n"
"min-height: 40px;\n"
"max-height: 40px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(193, 213, 243);\n"
"}\n"
"\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 8em;\n"
"    max-width: 200px;\n"
"    \n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgrey;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.framePanneauDeControle.setFrameShape(QtWidgets.QFrame.Box)
        self.framePanneauDeControle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePanneauDeControle.setLineWidth(2)
        self.framePanneauDeControle.setObjectName("framePanneauDeControle")
        self.gridLayout = QtWidgets.QGridLayout(self.framePanneauDeControle)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.titrePanneauDeControle = QtWidgets.QLabel(self.framePanneauDeControle)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.titrePanneauDeControle.setFont(font)
        self.titrePanneauDeControle.setAlignment(QtCore.Qt.AlignCenter)
        self.titrePanneauDeControle.setObjectName("titrePanneauDeControle")
        self.verticalLayout.addWidget(self.titrePanneauDeControle)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ajouterUnEquipementButton = QtWidgets.QPushButton(self.framePanneauDeControle)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Apprentissage Python/exercices/Hatim/Accueil/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ajouterUnEquipementButton.setIcon(icon)
        self.ajouterUnEquipementButton.setIconSize(QtCore.QSize(40, 40))
        self.ajouterUnEquipementButton.setObjectName("ajouterUnEquipementButton")
        self.verticalLayout.addWidget(self.ajouterUnEquipementButton)
        self.consulterUnEquipementButton = QtWidgets.QPushButton(self.framePanneauDeControle)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.consulterUnEquipementButton.setIcon(icon1)
        self.consulterUnEquipementButton.setIconSize(QtCore.QSize(40, 40))
        self.consulterUnEquipementButton.setObjectName("consulterUnEquipementButton")
        self.verticalLayout.addWidget(self.consulterUnEquipementButton)
        self.rechercherUnEquipementButton = QtWidgets.QPushButton(self.framePanneauDeControle)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rechercherUnEquipementButton.setIcon(icon2)
        self.rechercherUnEquipementButton.setIconSize(QtCore.QSize(40, 40))
        self.rechercherUnEquipementButton.setObjectName("rechercherUnEquipementButton")
        self.verticalLayout.addWidget(self.rechercherUnEquipementButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.ajouterBdtButton = QtWidgets.QPushButton(self.framePanneauDeControle)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ajouterBdtButton.setIcon(icon3)
        self.ajouterBdtButton.setIconSize(QtCore.QSize(40, 40))
        self.ajouterBdtButton.setObjectName("ajouterBdtButton")
        self.verticalLayout.addWidget(self.ajouterBdtButton)
        self.rechercherBdtButton = QtWidgets.QPushButton(self.framePanneauDeControle)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rechercherBdtButton.setIcon(icon4)
        self.rechercherBdtButton.setIconSize(QtCore.QSize(40, 40))
        self.rechercherBdtButton.setObjectName("rechercherBdtButton")
        self.verticalLayout.addWidget(self.rechercherBdtButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.statistiquesButton = QtWidgets.QPushButton(self.framePanneauDeControle)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("graph.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statistiquesButton.setIcon(icon5)
        self.statistiquesButton.setIconSize(QtCore.QSize(40, 40))
        self.statistiquesButton.setObjectName("statistiquesButton")
        self.verticalLayout.addWidget(self.statistiquesButton)
        self.imprimerButton = QtWidgets.QPushButton(self.framePanneauDeControle)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imprimerButton.setIcon(icon6)
        self.imprimerButton.setIconSize(QtCore.QSize(40, 40))
        self.imprimerButton.setObjectName("imprimerButton")
        self.verticalLayout.addWidget(self.imprimerButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.supportButton = QtWidgets.QPushButton(self.framePanneauDeControle)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("PC2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.supportButton.setIcon(icon7)
        self.supportButton.setIconSize(QtCore.QSize(40, 40))
        self.supportButton.setAutoDefault(False)
        self.supportButton.setDefault(False)
        self.supportButton.setFlat(False)
        self.supportButton.setObjectName("supportButton")
        self.verticalLayout.addWidget(self.supportButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.framePanneauDeControle, 0, 0, 2, 1)
        self.frameTitre = QtWidgets.QFrame(self.centralwidget)
        self.frameTitre.setStyleSheet("#frameTitre{\n"
"background-color: rgb(250, 250, 250);\n"
"max-height:110px;\n"
"}")
        self.frameTitre.setFrameShape(QtWidgets.QFrame.Box)
        self.frameTitre.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTitre.setLineWidth(2)
        self.frameTitre.setObjectName("frameTitre")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameTitre)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(289, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.titrePrincipal = QtWidgets.QLabel(self.frameTitre)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titrePrincipal.setFont(font)
        self.titrePrincipal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.titrePrincipal.setAlignment(QtCore.Qt.AlignCenter)
        self.titrePrincipal.setObjectName("titrePrincipal")
        self.horizontalLayout.addWidget(self.titrePrincipal)
        spacerItem5 = QtWidgets.QSpacerItem(258, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.titrePrincipal.raise_()
        self.gridLayout_4.addWidget(self.frameTitre, 0, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Frame = QtWidgets.QFrame(self.centralwidget)
        self.Frame.setStyleSheet("")
        self.Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame.setLineWidth(2)
        self.Frame.setObjectName("Frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.WidgetWindow = QtWidgets.QWidget(self.Frame)
        self.WidgetWindow.setObjectName("WidgetWindow")
        self.gridLayout_2.addWidget(self.WidgetWindow, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.Frame, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 1, 1, 1)
        self.frameTitre.raise_()
        self.framePanneauDeControle.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1219, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titrePanneauDeControle.setText(_translate("MainWindow", "Panneau\n"
" de contrôle"))
        self.ajouterUnEquipementButton.setText(_translate("MainWindow", "Ajouter un\n"
"équipement"))
        self.consulterUnEquipementButton.setText(_translate("MainWindow", "Consulter un\n"
"équipement"))
        self.rechercherUnEquipementButton.setText(_translate("MainWindow", "Rechercher un\n"
"équipement"))
        self.ajouterBdtButton.setText(_translate("MainWindow", "Ajouter un\n"
"bon de travail"))
        self.rechercherBdtButton.setText(_translate("MainWindow", "Rechercher un\n"
"bon de travail"))
        self.statistiquesButton.setText(_translate("MainWindow", "Voir les\n"
"statistiques"))
        self.imprimerButton.setText(_translate("MainWindow", "Imprimer tout\n"
"l\'inventaire"))
        self.supportButton.setText(_translate("MainWindow", "Support\n"
"technique"))
        self.titrePrincipal.setText(_translate("MainWindow", "S.I.M.M. 2.0\n"
"Hôpital Saint-Michel "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

