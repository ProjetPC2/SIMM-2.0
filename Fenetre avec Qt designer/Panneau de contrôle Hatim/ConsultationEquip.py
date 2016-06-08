# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConsultationEquip9.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainFrame(object):
    def setupUi(self, MainFrame):
        MainFrame.setObjectName("MainFrame")
        MainFrame.resize(905, 753)
        MainFrame.setStyleSheet("#MainFrame {\n"
"\n"
"background: white;\n"
"}\n"
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
"background-color: rgb(219, 231, 248);\n"
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
        self.gridLayout = QtWidgets.QGridLayout(MainFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titre = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.titre.setFont(font)
        self.titre.setObjectName("titre")
        self.horizontalLayout.addWidget(self.titre)
        self.label = QtWidgets.QLabel(MainFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("book.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lineEdit = QtWidgets.QLineEdit(MainFrame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.afficherEquipementButton = QtWidgets.QPushButton(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.afficherEquipementButton.setFont(font)
        self.afficherEquipementButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.afficherEquipementButton.setIcon(icon)
        self.afficherEquipementButton.setIconSize(QtCore.QSize(36, 36))
        self.afficherEquipementButton.setObjectName("afficherEquipementButton")
        self.verticalLayout_3.addWidget(self.afficherEquipementButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 3, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ajouterUnEquipementNutton = QtWidgets.QPushButton(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ajouterUnEquipementNutton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ajouterUnEquipementNutton.setIcon(icon1)
        self.ajouterUnEquipementNutton.setIconSize(QtCore.QSize(42, 42))
        self.ajouterUnEquipementNutton.setObjectName("ajouterUnEquipementNutton")
        self.horizontalLayout_4.addWidget(self.ajouterUnEquipementNutton)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5, 0, QtCore.Qt.AlignRight)
        self.label_28 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.verticalLayout.addWidget(self.label_28, 0, QtCore.Qt.AlignRight)
        self.label_32 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.verticalLayout.addWidget(self.label_32)
        self.label_30 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.verticalLayout.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.verticalLayout.addWidget(self.label_31)
        self.label_33 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.verticalLayout.addWidget(self.label_33)
        self.label_29 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.verticalLayout.addWidget(self.label_29)
        self.label_27 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.verticalLayout.addWidget(self.label_27)
        self.label_26 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.verticalLayout.addWidget(self.label_26)
        self.label_14 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_17 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_35 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_2.addWidget(self.label_35)
        self.label_36 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_2.addWidget(self.label_36)
        self.label_37 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_2.addWidget(self.label_37)
        self.label_38 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_2.addWidget(self.label_38)
        self.label_39 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_2.addWidget(self.label_39)
        self.label_40 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_2.addWidget(self.label_40)
        self.label_41 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_2.addWidget(self.label_41)
        self.label_42 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_2.addWidget(self.label_42)
        self.label_43 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_43.setFont(font)
        self.label_43.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_43.setObjectName("label_43")
        self.verticalLayout_2.addWidget(self.label_43)
        self.label_44 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_44.setFont(font)
        self.label_44.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_2.addWidget(self.label_44)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 2, 1, 2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_34 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_7.addWidget(self.label_34, 0, QtCore.Qt.AlignRight)
        self.gridLayout.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_45 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_45.setFont(font)
        self.label_45.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName("label_45")
        self.horizontalLayout_5.addWidget(self.label_45)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 1, 1, 3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_46 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_46.setFont(font)
        self.label_46.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.horizontalLayout_8.addWidget(self.label_46)
        self.gridLayout.addLayout(self.horizontalLayout_8, 5, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.comboBox = QtWidgets.QComboBox(MainFrame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setMaxCount(2147483645)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setObjectName("comboBox")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("view-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon2, "")
        self.comboBox.addItem(icon2, "")
        self.comboBox.addItem(icon2, "")
        self.horizontalLayout_6.addWidget(self.comboBox, 0, QtCore.Qt.AlignLeft)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 1, 1, 2)

        self.retranslateUi(MainFrame)
        QtCore.QMetaObject.connectSlotsByName(MainFrame)

    def retranslateUi(self, MainFrame):
        _translate = QtCore.QCoreApplication.translate
        MainFrame.setWindowTitle(_translate("MainFrame", "Form"))
        self.titre.setText(_translate("MainFrame", "Consultation / Modification d\'équipement"))
        self.label_6.setText(_translate("MainFrame", "  Entrez le numéro d\'ID :"))
        self.ajouterUnEquipementNutton.setText(_translate("MainFrame", "Modifier l\'équipement "))
        self.label_5.setText(_translate("MainFrame", "Catégorie : "))
        self.label_28.setText(_translate("MainFrame", "Marque : "))
        self.label_32.setText(_translate("MainFrame", "Modèle : "))
        self.label_30.setText(_translate("MainFrame", "No. de série : "))
        self.label_31.setText(_translate("MainFrame", "Salle : "))
        self.label_33.setText(_translate("MainFrame", "Centre de service : "))
        self.label_29.setText(_translate("MainFrame", "Date d\'aquisition : "))
        self.label_27.setText(_translate("MainFrame", "Date du dernier entretien : "))
        self.label_26.setText(_translate("MainFrame", "Provenance : "))
        self.label_14.setText(_translate("MainFrame", "État de service : "))
        self.label_17.setText(_translate("MainFrame", "État de conservation : "))
        self.label_7.setText(_translate("MainFrame", "Équipement de Néonatologie"))
        self.label_35.setText(_translate("MainFrame", "Bosch"))
        self.label_36.setText(_translate("MainFrame", "XR310b"))
        self.label_37.setText(_translate("MainFrame", "A265XG680H"))
        self.label_38.setText(_translate("MainFrame", "C-7612"))
        self.label_39.setText(_translate("MainFrame", "Unité des soins intensifs (Néonatologie)"))
        self.label_40.setText(_translate("MainFrame", "2015-10-05"))
        self.label_41.setText(_translate("MainFrame", "2016-01-22"))
        self.label_42.setText(_translate("MainFrame", "Suisse"))
        self.label_43.setText(_translate("MainFrame", "Excellent"))
        self.label_44.setText(_translate("MainFrame", "Non-Périmable"))
        self.label_34.setText(_translate("MainFrame", "Commentaires : "))
        self.label_45.setText(_translate("MainFrame", "Ici se trouveront des commentaires consernant\n"
"l\'équipement en question et pourront être de toute nature.\n"
"Le commentaire peut être assez long, comme vous pouvez le constater, mais\n"
"vous ne pouvez vous arrêter de le lire, car\n"
"nous sommes programmés ainsi."))
        self.label_46.setText(_translate("MainFrame", "Bons : "))
        self.comboBox.setItemText(0, _translate("MainFrame", "Bon 2016-01-22"))
        self.comboBox.setItemText(1, _translate("MainFrame", "Bon 2016-03-07"))
        self.comboBox.setItemText(2, _translate("MainFrame", "Bon 2016-05-12"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QWidget()
    ui = Ui_MainFrame()
    ui.setupUi(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())

