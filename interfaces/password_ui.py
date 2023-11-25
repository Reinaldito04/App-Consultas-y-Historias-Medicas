# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/password.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(531, 399)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("QFrame{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.505682 , x2:1 , y2:0.477,stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));\n"
"color:white;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_menu = QtWidgets.QPushButton(self.frame)
        self.bt_menu.setMinimumSize(QtCore.QSize(60, 60))
        self.bt_menu.setMaximumSize(QtCore.QSize(60, 60))
        self.bt_menu.setStyleSheet("QPushButton{\n"
"border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:rgb(145, 200, 228);\n"
"\n"
"}\n"
"")
        self.bt_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/casa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QtCore.QSize(38, 38))
        self.bt_menu.setObjectName("bt_menu")
        self.horizontalLayout.addWidget(self.bt_menu)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"background-color:none;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.bt_salir = QtWidgets.QPushButton(self.frame)
        self.bt_salir.setMinimumSize(QtCore.QSize(60, 60))
        self.bt_salir.setMaximumSize(QtCore.QSize(60, 60))
        self.bt_salir.setStyleSheet("QPushButton{\n"
"border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:rgb(145, 200, 228);\n"
"\n"
"}\n"
"")
        self.bt_salir.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/exit-fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_salir.setIcon(icon1)
        self.bt_salir.setIconSize(QtCore.QSize(38, 38))
        self.bt_salir.setObjectName("bt_salir")
        self.horizontalLayout.addWidget(self.bt_salir)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.txt_passwordOld = QtWidgets.QLineEdit(self.frame)
        self.txt_passwordOld.setMinimumSize(QtCore.QSize(400, 50))
        self.txt_passwordOld.setMaximumSize(QtCore.QSize(400, 50))
        self.txt_passwordOld.setStyleSheet("QLineEdit{\n"
"  height: 40px;\n"
"  padding: 10px;\n"
"  border: 4px solid #17202A;\n"
"  border-radius: 10px;\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.txt_passwordOld.setText("")
        self.txt_passwordOld.setObjectName("txt_passwordOld")
        self.verticalLayout.addWidget(self.txt_passwordOld)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.txt_passwordNew = QtWidgets.QLineEdit(self.frame)
        self.txt_passwordNew.setMinimumSize(QtCore.QSize(400, 50))
        self.txt_passwordNew.setMaximumSize(QtCore.QSize(400, 50))
        self.txt_passwordNew.setStyleSheet("QLineEdit{\n"
"  height: 40px;\n"
"  padding: 10px;\n"
"  border: 4px solid #17202A;\n"
"  border-radius: 10px;\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.txt_passwordNew.setText("")
        self.txt_passwordNew.setObjectName("txt_passwordNew")
        self.verticalLayout.addWidget(self.txt_passwordNew)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.txt_passowrdRepeat = QtWidgets.QLineEdit(self.frame)
        self.txt_passowrdRepeat.setMinimumSize(QtCore.QSize(400, 50))
        self.txt_passowrdRepeat.setMaximumSize(QtCore.QSize(400, 50))
        self.txt_passowrdRepeat.setStyleSheet("QLineEdit{\n"
"  height: 40px;\n"
"  padding: 10px;\n"
"  border: 4px solid #17202A;\n"
"  border-radius: 10px;\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.txt_passowrdRepeat.setText("")
        self.txt_passowrdRepeat.setObjectName("txt_passowrdRepeat")
        self.verticalLayout.addWidget(self.txt_passowrdRepeat)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.bt_passwordChange = QtWidgets.QPushButton(self.frame)
        self.bt_passwordChange.setMinimumSize(QtCore.QSize(250, 60))
        self.bt_passwordChange.setMaximumSize(QtCore.QSize(250, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.bt_passwordChange.setFont(font)
        self.bt_passwordChange.setStyleSheet("QPushButton{\n"
"border-radius:25px;\n"
"    font: 12pt \"Microsoft Sans Serif\";\n"
"color:white;\n"
"background-color:rgba(145, 200, 228,80);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:rgb(145, 200, 228);\n"
"\n"
"}\n"
"\n"
"")
        self.bt_passwordChange.setIconSize(QtCore.QSize(38, 38))
        self.bt_passwordChange.setObjectName("bt_passwordChange")
        self.horizontalLayout_2.addWidget(self.bt_passwordChange)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Menú para cambio de contraseña"))
        self.txt_passwordOld.setPlaceholderText(_translate("Dialog", "Contraseña actual"))
        self.txt_passwordNew.setPlaceholderText(_translate("Dialog", "Nueva contraseña"))
        self.txt_passowrdRepeat.setPlaceholderText(_translate("Dialog", "Repita la nueva contraseña"))
        self.bt_passwordChange.setText(_translate("Dialog", "Cambiar Contraseña"))
