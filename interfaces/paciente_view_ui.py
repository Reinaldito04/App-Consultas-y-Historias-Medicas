# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/paciente_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pacientes_view(object):
    def setupUi(self, pacientes_view):
        pacientes_view.setObjectName("pacientes_view")
        pacientes_view.resize(988, 718)
        self.centralwidget = QtWidgets.QWidget(pacientes_view)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"background-color:rgb(0, 85, 127);\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(25, 25))
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("QFrame{\n"
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
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.filtro = QtWidgets.QComboBox(self.frame_2)
        self.filtro.setMinimumSize(QtCore.QSize(300, 40))
        self.filtro.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.filtro.setFont(font)
        self.filtro.setAutoFillBackground(False)
        self.filtro.setStyleSheet("")
        self.filtro.setFrame(False)
        self.filtro.setObjectName("filtro")
        self.horizontalLayout.addWidget(self.filtro)
        self.in_buscar = QtWidgets.QLineEdit(self.frame_2)
        self.in_buscar.setMinimumSize(QtCore.QSize(200, 40))
        self.in_buscar.setMaximumSize(QtCore.QSize(200, 40))
        self.in_buscar.setInputMask("")
        self.in_buscar.setText("")
        self.in_buscar.setMaxLength(20)
        self.in_buscar.setPlaceholderText("")
        self.in_buscar.setObjectName("in_buscar")
        self.horizontalLayout.addWidget(self.in_buscar)
        self.bt_buscar = QtWidgets.QPushButton(self.frame_2)
        self.bt_buscar.setMinimumSize(QtCore.QSize(80, 40))
        self.bt_buscar.setMaximumSize(QtCore.QSize(80, 40))
        self.bt_buscar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/buscar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_buscar.setIcon(icon)
        self.bt_buscar.setIconSize(QtCore.QSize(30, 30))
        self.bt_buscar.setObjectName("bt_buscar")
        self.horizontalLayout.addWidget(self.bt_buscar)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bt_act = QtWidgets.QPushButton(self.frame_2)
        self.bt_act.setMinimumSize(QtCore.QSize(150, 50))
        self.bt_act.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bt_act.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/actualizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_act.setIcon(icon1)
        self.bt_act.setIconSize(QtCore.QSize(30, 30))
        self.bt_act.setObjectName("bt_act")
        self.horizontalLayout_3.addWidget(self.bt_act)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.bt_preview = QtWidgets.QPushButton(self.frame_2)
        self.bt_preview.setMinimumSize(QtCore.QSize(150, 50))
        self.bt_preview.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bt_preview.setFont(font)
        self.bt_preview.setIconSize(QtCore.QSize(30, 30))
        self.bt_preview.setObjectName("bt_preview")
        self.horizontalLayout_3.addWidget(self.bt_preview)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabla_p = QtWidgets.QTableWidget(self.frame_3)
        self.tabla_p.setObjectName("tabla_p")
        self.tabla_p.setColumnCount(9)
        self.tabla_p.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_p.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_p.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_p.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_p.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_p.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_p.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_p.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_p.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_p.setHorizontalHeaderItem(8, item)
        self.tabla_p.horizontalHeader().setDefaultSectionSize(170)
        self.tabla_p.horizontalHeader().setMinimumSectionSize(100)
        self.tabla_p.horizontalHeader().setSortIndicatorShown(False)
        self.tabla_p.horizontalHeader().setStretchLastSection(True)
        self.tabla_p.verticalHeader().setVisible(True)
        self.verticalLayout_4.addWidget(self.tabla_p)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.verticalLayout_3.addWidget(self.frame_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/silla-de-dentista.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.frame)
        pacientes_view.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(pacientes_view)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 988, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        pacientes_view.setMenuBar(self.menubar)
        self.actionVolver_al_registro = QtWidgets.QAction(pacientes_view)
        self.actionVolver_al_registro.setObjectName("actionVolver_al_registro")
        self.actionVolver_al_menu_principal = QtWidgets.QAction(pacientes_view)
        self.actionVolver_al_menu_principal.setObjectName("actionVolver_al_menu_principal")
        self.actionSalir = QtWidgets.QAction(pacientes_view)
        self.actionSalir.setObjectName("actionSalir")
        self.menuMenu.addAction(self.actionVolver_al_menu_principal)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionSalir)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(pacientes_view)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(pacientes_view)

    def retranslateUi(self, pacientes_view):
        _translate = QtCore.QCoreApplication.translate
        pacientes_view.setWindowTitle(_translate("pacientes_view", "MainWindow"))
        self.label.setText(_translate("pacientes_view", "Visualización de pacientes"))
        self.bt_act.setText(_translate("pacientes_view", "Actualizar tabla"))
        self.bt_preview.setText(_translate("pacientes_view", "Guardar PDF"))
        item = self.tabla_p.horizontalHeaderItem(0)
        item.setText(_translate("pacientes_view", "ID"))
        item = self.tabla_p.horizontalHeaderItem(1)
        item.setText(_translate("pacientes_view", "Nombre de usuario"))
        item = self.tabla_p.horizontalHeaderItem(2)
        item.setText(_translate("pacientes_view", "Cedula"))
        item = self.tabla_p.horizontalHeaderItem(3)
        item.setText(_translate("pacientes_view", "Nombres"))
        item = self.tabla_p.horizontalHeaderItem(4)
        item.setText(_translate("pacientes_view", "Apellidos"))
        item = self.tabla_p.horizontalHeaderItem(5)
        item.setText(_translate("pacientes_view", "Edad"))
        item = self.tabla_p.horizontalHeaderItem(6)
        item.setText(_translate("pacientes_view", "Sexo"))
        item = self.tabla_p.horizontalHeaderItem(7)
        item.setText(_translate("pacientes_view", "Telefono"))
        item = self.tabla_p.horizontalHeaderItem(8)
        item.setText(_translate("pacientes_view", "Fecha_Diagnotico"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("pacientes_view", "Pacientes registrados"))
        self.menuMenu.setTitle(_translate("pacientes_view", "Menu"))
        self.actionVolver_al_registro.setText(_translate("pacientes_view", "Volver al registro"))
        self.actionVolver_al_menu_principal.setText(_translate("pacientes_view", "Volver al menu principal"))
        self.actionSalir.setText(_translate("pacientes_view", "Salir"))
