# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'users.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(842, 445)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("QFrame{\n"
"background-color:rgb(0, 85, 127);\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_5 = QtWidgets.QFrame(self.tab_3)
        self.frame_5.setStyleSheet("QFrame{\n"
"background-color:rgb(70, 130, 169);\n"
"    font: 14pt \"Microsoft Sans Serif\";\n"
"}\n"
"QTableWidget{\n"
"color:rgb(0,0,0);\n"
"gridline-color:rgb(0,206,151);\n"
"font-size:12pt;\n"
"}\n"
"QHeaderView::section{\n"
"background-color:rgb(0,206,151);\n"
"border:1px solid rgb(0,0,0);\n"
"    font: 12pt \"Microsoft Sans Serif\";\n"
"}\n"
"QTbaleWidget QTableCornerButton::section{\n"
"background-color:rgb(0,0,0);\n"
"border:1px solid  rgb(0,206,151);\n"
"}\n"
"QLineEdit{\n"
"border:2px solid rgb(0,0,0);\n"
"border-radius:20px;\n"
"    font: 12pt \"Microsoft Sans Serif\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"border-radius:20px;\n"
"border:2px solid rgb(0,0,0);\n"
"background-color:white;\n"
"    font: 11pt \"Microsoft Sans Serif\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#5DADE2;\n"
"}\n"
"QTextEdit{\n"
"border:4px solid rgb(0,0,0);\n"
"border-radius:20px;\n"
"    font: 12pt \"Microsoft Sans Serif\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"    background-color:#5DADE2;\n"
"}\n"
"QRadioButton{\n"
"    font: 14pt \"Microsoft Sans Serif\";\n"
"}\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QFrame{\n"
"background-color:rgb(70, 130, 169);\n"
"    font: 14pt \"Microsoft Sans Serif\";\n"
"}\n"
"QTableWidget{\n"
"color:rgb(0,0,0);\n"
"gridline-color:rgb(0,206,151);\n"
"font-size:12pt;\n"
"}\n"
"QHeaderView::section{\n"
"background-color:rgb(0,206,151);\n"
"border:1px solid rgb(0,0,0);\n"
"    font: 12pt \"Microsoft Sans Serif\";\n"
"}\n"
"QTbaleWidget QTableCornerButton::section{\n"
"background-color:rgb(0,0,0);\n"
"border:1px solid  rgb(0,206,151);\n"
"}\n"
"QLineEdit{\n"
"border:2px solid rgb(0,0,0);\n"
"border-radius:20px;\n"
"    font: 12pt \"Microsoft Sans Serif\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"border-radius:20px;\n"
"border:2px solid rgb(0,0,0);\n"
"background-color:white;\n"
"    font: 11pt \"Microsoft Sans Serif\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#5DADE2;\n"
"}\n"
"QTextEdit{\n"
"border:4px solid rgb(0,0,0);\n"
"border-radius:20px;\n"
"    font: 12pt \"Microsoft Sans Serif\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"    background-color:#5DADE2;\n"
"}\n"
"QRadioButton{\n"
"    font: 14pt \"Microsoft Sans Serif\";\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.frame_5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_7.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(393, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lbl_username = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_username.setFont(font)
        self.lbl_username.setObjectName("lbl_username")
        self.horizontalLayout_11.addWidget(self.lbl_username)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.in_user = QtWidgets.QLineEdit(self.frame_5)
        self.in_user.setMinimumSize(QtCore.QSize(200, 40))
        self.in_user.setMaximumSize(QtCore.QSize(200, 40))
        self.in_user.setObjectName("in_user")
        self.horizontalLayout_11.addWidget(self.in_user)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        spacerItem2 = QtWidgets.QSpacerItem(393, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.lbl_password = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_password.setFont(font)
        self.lbl_password.setObjectName("lbl_password")
        self.horizontalLayout_20.addWidget(self.lbl_password)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem3)
        self.in_password = QtWidgets.QLineEdit(self.frame_5)
        self.in_password.setMinimumSize(QtCore.QSize(200, 40))
        self.in_password.setMaximumSize(QtCore.QSize(200, 40))
        self.in_password.setObjectName("in_password")
        self.horizontalLayout_20.addWidget(self.in_password)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        spacerItem4 = QtWidgets.QSpacerItem(393, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.lbl_password_2 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_password_2.setFont(font)
        self.lbl_password_2.setObjectName("lbl_password_2")
        self.horizontalLayout_23.addWidget(self.lbl_password_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem5)
        self.in_conf = QtWidgets.QLineEdit(self.frame_5)
        self.in_conf.setMinimumSize(QtCore.QSize(200, 40))
        self.in_conf.setMaximumSize(QtCore.QSize(200, 40))
        self.in_conf.setObjectName("in_conf")
        self.horizontalLayout_23.addWidget(self.in_conf)
        self.verticalLayout_2.addLayout(self.horizontalLayout_23)
        spacerItem6 = QtWidgets.QSpacerItem(393, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(13, 337, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lbl_level = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_level.setFont(font)
        self.lbl_level.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_level.setObjectName("lbl_level")
        self.verticalLayout_5.addWidget(self.lbl_level)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bt_admin = QtWidgets.QRadioButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.bt_admin.setFont(font)
        self.bt_admin.setCheckable(False)
        self.bt_admin.setObjectName("bt_admin")
        self.verticalLayout_3.addWidget(self.bt_admin)
        self.bt_doc = QtWidgets.QRadioButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.bt_doc.setFont(font)
        self.bt_doc.setObjectName("bt_doc")
        self.verticalLayout_3.addWidget(self.bt_doc)
        self.bt_user = QtWidgets.QRadioButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.bt_user.setFont(font)
        self.bt_user.setObjectName("bt_user")
        self.verticalLayout_3.addWidget(self.bt_user)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem8)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        spacerItem9 = QtWidgets.QSpacerItem(13, 337, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setStyleSheet("QLabel{\n"
"background-color:white;\n"
"border-right:2px solid rgb(0,0,0);\n"
"border-left:2px solid rgb(0,0,0);\n"
"border-top:2px solid rgb(0,0,0);\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_18.addWidget(self.label_2)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setStyleSheet("QFrame{\n"
"    background-color:#707B7C;\n"
"border-right:2px solid rgb(0,0,0);\n"
"border-left:2px solid rgb(0,0,0);\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"border-top:2px solid rgb(0,0,0);\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(spacerItem10)
        self.btn_agg = QtWidgets.QPushButton(self.frame_7)
        self.btn_agg.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_agg.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_agg.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ELEMENTOS GRAFICOS/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_agg.setIcon(icon)
        self.btn_agg.setIconSize(QtCore.QSize(25, 25))
        self.btn_agg.setObjectName("btn_agg")
        self.verticalLayout_20.addWidget(self.btn_agg)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(spacerItem11)
        self.btn_clear = QtWidgets.QPushButton(self.frame_7)
        self.btn_clear.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_clear.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_clear.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ELEMENTOS GRAFICOS/limpiar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_clear.setIcon(icon1)
        self.btn_clear.setIconSize(QtCore.QSize(25, 25))
        self.btn_clear.setObjectName("btn_clear")
        self.verticalLayout_20.addWidget(self.btn_clear)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(spacerItem12)
        self.verticalLayout_19.addLayout(self.verticalLayout_20)
        self.verticalLayout_18.addWidget(self.frame_7)
        self.verticalLayout_4.addLayout(self.verticalLayout_18)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        spacerItem14 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem14)
        self.verticalLayout_21.addWidget(self.frame_5)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_13.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Registro de usuario"))
        self.lbl_username.setText(_translate("Dialog", "Nombre de usuario"))
        self.lbl_password.setText(_translate("Dialog", "Contraseña"))
        self.lbl_password_2.setText(_translate("Dialog", "Confirme su contraseña"))
        self.lbl_level.setText(_translate("Dialog", "Niveles de acceso"))
        self.bt_admin.setText(_translate("Dialog", "Admin"))
        self.bt_doc.setText(_translate("Dialog", "Doctor"))
        self.bt_user.setText(_translate("Dialog", "Persona"))
        self.label_2.setText(_translate("Dialog", "Controles"))
        self.btn_agg.setText(_translate("Dialog", "Agregar"))
        self.btn_clear.setText(_translate("Dialog", "Limpiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Registro de datos de usuario"))
