# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/edicion.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(994, 574)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"background-color:rgb(0, 85, 127);\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.tab)
        self.frame_3.setStyleSheet("QFrame{\n"
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
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.foto_2 = QtWidgets.QLabel(self.frame_3)
        self.foto_2.setMinimumSize(QtCore.QSize(150, 150))
        self.foto_2.setMaximumSize(QtCore.QSize(150, 150))
        self.foto_2.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(0, 0, 0);\n"
"}")
        self.foto_2.setScaledContents(True)
        self.foto_2.setAlignment(QtCore.Qt.AlignCenter)
        self.foto_2.setObjectName("foto_2")
        self.verticalLayout_9.addWidget(self.foto_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.horizontalLayout_14.addLayout(self.verticalLayout_9)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_cedul_2 = QtWidgets.QLabel(self.frame_3)
        self.lbl_cedul_2.setObjectName("lbl_cedul_2")
        self.horizontalLayout_2.addWidget(self.lbl_cedul_2)
        self.in_cedula_2 = QtWidgets.QLineEdit(self.frame_3)
        self.in_cedula_2.setMinimumSize(QtCore.QSize(200, 40))
        self.in_cedula_2.setMaximumSize(QtCore.QSize(200, 40))
        self.in_cedula_2.setMaxLength(20)
        self.in_cedula_2.setObjectName("in_cedula_2")
        self.horizontalLayout_2.addWidget(self.in_cedula_2)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_espec_2 = QtWidgets.QLabel(self.frame_3)
        self.lbl_espec_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_espec_2.setObjectName("lbl_espec_2")
        self.horizontalLayout_5.addWidget(self.lbl_espec_2)
        self.in_espec_2 = QtWidgets.QLineEdit(self.frame_3)
        self.in_espec_2.setMinimumSize(QtCore.QSize(200, 40))
        self.in_espec_2.setMaximumSize(QtCore.QSize(200, 40))
        self.in_espec_2.setObjectName("in_espec_2")
        self.horizontalLayout_5.addWidget(self.in_espec_2)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_name_2 = QtWidgets.QLabel(self.frame_3)
        self.lbl_name_2.setObjectName("lbl_name_2")
        self.horizontalLayout_3.addWidget(self.lbl_name_2)
        self.in_name_2 = QtWidgets.QLineEdit(self.frame_3)
        self.in_name_2.setMinimumSize(QtCore.QSize(200, 40))
        self.in_name_2.setMaximumSize(QtCore.QSize(200, 40))
        self.in_name_2.setObjectName("in_name_2")
        self.horizontalLayout_3.addWidget(self.in_name_2)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbl_apell_2 = QtWidgets.QLabel(self.frame_3)
        self.lbl_apell_2.setObjectName("lbl_apell_2")
        self.horizontalLayout_6.addWidget(self.lbl_apell_2)
        self.in_apell_2 = QtWidgets.QLineEdit(self.frame_3)
        self.in_apell_2.setMinimumSize(QtCore.QSize(200, 40))
        self.in_apell_2.setMaximumSize(QtCore.QSize(200, 40))
        self.in_apell_2.setObjectName("in_apell_2")
        self.horizontalLayout_6.addWidget(self.in_apell_2)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem4)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lbl_number_2 = QtWidgets.QLabel(self.frame_3)
        self.lbl_number_2.setObjectName("lbl_number_2")
        self.horizontalLayout_7.addWidget(self.lbl_number_2)
        self.in_number_2 = QtWidgets.QLineEdit(self.frame_3)
        self.in_number_2.setMinimumSize(QtCore.QSize(200, 40))
        self.in_number_2.setMaximumSize(QtCore.QSize(200, 40))
        self.in_number_2.setObjectName("in_number_2")
        self.horizontalLayout_7.addWidget(self.in_number_2)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lbl_age_2 = QtWidgets.QLabel(self.frame_3)
        self.lbl_age_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_age_2.setObjectName("lbl_age_2")
        self.horizontalLayout_9.addWidget(self.lbl_age_2)
        self.in_age_2 = QtWidgets.QLineEdit(self.frame_3)
        self.in_age_2.setMinimumSize(QtCore.QSize(80, 40))
        self.in_age_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.in_age_2.setMaxLength(2)
        self.in_age_2.setAlignment(QtCore.Qt.AlignCenter)
        self.in_age_2.setClearButtonEnabled(False)
        self.in_age_2.setObjectName("in_age_2")
        self.horizontalLayout_9.addWidget(self.in_age_2)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_gen_2 = QtWidgets.QLabel(self.frame_3)
        self.lbl_gen_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_gen_2.setObjectName("lbl_gen_2")
        self.horizontalLayout.addWidget(self.lbl_gen_2)
        self.btn_m_2 = QtWidgets.QRadioButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_m_2.setFont(font)
        self.btn_m_2.setStyleSheet("")
        self.btn_m_2.setObjectName("btn_m_2")
        self.horizontalLayout.addWidget(self.btn_m_2)
        self.btn_f_2 = QtWidgets.QRadioButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_f_2.setFont(font)
        self.btn_f_2.setObjectName("btn_f_2")
        self.horizontalLayout.addWidget(self.btn_f_2)
        self.horizontalLayout_11.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem6)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_dir_2 = QtWidgets.QLabel(self.frame_3)
        self.lbl_dir_2.setObjectName("lbl_dir_2")
        self.horizontalLayout_4.addWidget(self.lbl_dir_2)
        self.in_dir_2 = QtWidgets.QLineEdit(self.frame_3)
        self.in_dir_2.setMinimumSize(QtCore.QSize(200, 40))
        self.in_dir_2.setMaximumSize(QtCore.QSize(200, 40))
        self.in_dir_2.setObjectName("in_dir_2")
        self.horizontalLayout_4.addWidget(self.in_dir_2)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lbl_mail_2 = QtWidgets.QLabel(self.frame_3)
        self.lbl_mail_2.setObjectName("lbl_mail_2")
        self.horizontalLayout_8.addWidget(self.lbl_mail_2)
        self.in_mail_2 = QtWidgets.QLineEdit(self.frame_3)
        self.in_mail_2.setMinimumSize(QtCore.QSize(200, 40))
        self.in_mail_2.setMaximumSize(QtCore.QSize(200, 40))
        self.in_mail_2.setObjectName("in_mail_2")
        self.horizontalLayout_8.addWidget(self.in_mail_2)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_8)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.horizontalLayout_14.addLayout(self.verticalLayout_8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem10)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setStyleSheet("QLabel{\n"
"background-color:white;\n"
"border-right:2px solid rgb(0,0,0);\n"
"border-left:2px solid rgb(0,0,0);\n"
"border-top:2px solid rgb(0,0,0);\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setStyleSheet("QFrame{    \n"
"background-color:#707B7C;\n"
"border-right:2px solid rgb(0,0,0);\n"
"border-left:2px solid rgb(0,0,0);\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"border-top:2px solid rgb(0,0,0);\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem11)
        self.btn_save = QtWidgets.QPushButton(self.frame_5)
        self.btn_save.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_save.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_save.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon)
        self.btn_save.setIconSize(QtCore.QSize(25, 25))
        self.btn_save.setObjectName("btn_save")
        self.verticalLayout_3.addWidget(self.btn_save)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem12)
        self.btn_passwordChange = QtWidgets.QPushButton(self.frame_5)
        self.btn_passwordChange.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_passwordChange.setMaximumSize(QtCore.QSize(150, 50))
        self.btn_passwordChange.setObjectName("btn_passwordChange")
        self.verticalLayout_3.addWidget(self.btn_passwordChange)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem13)
        self.bt_delete = QtWidgets.QPushButton(self.frame_5)
        self.bt_delete.setMinimumSize(QtCore.QSize(150, 50))
        self.bt_delete.setObjectName("bt_delete")
        self.verticalLayout_3.addWidget(self.bt_delete)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem14)
        self.btn_adduser = QtWidgets.QPushButton(self.frame_5)
        self.btn_adduser.setMinimumSize(QtCore.QSize(150, 50))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/agregar-usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_adduser.setIcon(icon1)
        self.btn_adduser.setIconSize(QtCore.QSize(25, 25))
        self.btn_adduser.setObjectName("btn_adduser")
        self.verticalLayout_3.addWidget(self.btn_adduser)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem15)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addWidget(self.frame_5)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem16)
        self.horizontalLayout_14.addLayout(self.verticalLayout_6)
        self.verticalLayout_10.addLayout(self.horizontalLayout_14)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem17)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_5.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 994, 21))
        self.menubar.setObjectName("menubar")
        self.menuMen = QtWidgets.QMenu(self.menubar)
        self.menuMen.setObjectName("menuMen")
        MainWindow.setMenuBar(self.menubar)
        self.actionBack = QtWidgets.QAction(MainWindow)
        self.actionBack.setObjectName("actionBack")
        self.menuMen.addAction(self.actionBack)
        self.menubar.addAction(self.menuMen.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Su foto es:"))
        self.foto_2.setText(_translate("MainWindow", "Foto"))
        self.lbl_cedul_2.setText(_translate("MainWindow", "Cedula:"))
        self.lbl_espec_2.setText(_translate("MainWindow", "Especialidad:"))
        self.lbl_name_2.setText(_translate("MainWindow", "Nombre:"))
        self.lbl_apell_2.setText(_translate("MainWindow", "Apellido:"))
        self.lbl_number_2.setText(_translate("MainWindow", "Telefono:"))
        self.lbl_age_2.setText(_translate("MainWindow", "Edad:"))
        self.lbl_gen_2.setText(_translate("MainWindow", "Sexo:"))
        self.btn_m_2.setText(_translate("MainWindow", "M"))
        self.btn_f_2.setText(_translate("MainWindow", "F"))
        self.lbl_dir_2.setText(_translate("MainWindow", "Dirección:"))
        self.lbl_mail_2.setText(_translate("MainWindow", "E-mail:"))
        self.label_2.setText(_translate("MainWindow", "Controles"))
        self.btn_save.setText(_translate("MainWindow", "Modificar"))
        self.btn_passwordChange.setText(_translate("MainWindow", "Cambiar contraseña"))
        self.bt_delete.setText(_translate("MainWindow", "Eliminar usuario"))
        self.btn_adduser.setText(_translate("MainWindow", "Añadir usuarios"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Edicion de datos del usuario"))
        self.menuMen.setTitle(_translate("MainWindow", "Menú"))
        self.actionBack.setText(_translate("MainWindow", "Volver al menú prinicpal"))
