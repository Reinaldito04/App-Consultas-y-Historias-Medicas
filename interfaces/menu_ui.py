# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1149, 874)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"background-color:rgb(70, 130, 169);\n"
"\n"
"}\n"
"QTableWidget{\n"
"color:rgb(0,0,0);\n"
"gridline-color:rgb(0,206,151);\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QHeaderView::section{\n"
"background-color:rgb(0,206,151);\n"
"border:1px solid rgb(0,0,0);\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QTbaleWidget QTableCornerButton::section{\n"
"background-color:rgb(0,0,0);\n"
"border:1px solid  rgb(0,206,151);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_superior = QtWidgets.QFrame(self.frame)
        self.frame_superior.setEnabled(True)
        self.frame_superior.setMinimumSize(QtCore.QSize(0, 65))
        self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_superior.setStyleSheet("QFrame{\n"
"background-color:rgb(0, 85, 127);\n"
"border-radius:25px;\n"
"}")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_menu = QtWidgets.QPushButton(self.frame_superior)
        self.bt_menu.setMinimumSize(QtCore.QSize(50, 50))
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
        icon.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/bar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QtCore.QSize(45, 45))
        self.bt_menu.setObjectName("bt_menu")
        self.horizontalLayout_2.addWidget(self.bt_menu)
        self.bt_bdd = QtWidgets.QPushButton(self.frame_superior)
        self.bt_bdd.setMinimumSize(QtCore.QSize(50, 50))
        self.bt_bdd.setStyleSheet("QPushButton{\n"
"border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:rgb(145, 200, 228);\n"
"\n"
"}\n"
"")
        self.bt_bdd.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/archivo-de-base-de-datos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_bdd.setIcon(icon1)
        self.bt_bdd.setIconSize(QtCore.QSize(45, 45))
        self.bt_bdd.setObjectName("bt_bdd")
        self.horizontalLayout_2.addWidget(self.bt_bdd)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_10 = QtWidgets.QLabel(self.frame_superior)
        self.label_10.setStyleSheet("font: 26pt \"MS Reference Sans Serif\";")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.bt_help = QtWidgets.QPushButton(self.frame_superior)
        self.bt_help.setMinimumSize(QtCore.QSize(50, 50))
        self.bt_help.setStyleSheet("QPushButton{\n"
"border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:rgb(145, 200, 228);\n"
"\n"
"}")
        self.bt_help.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/informacion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_help.setIcon(icon2)
        self.bt_help.setIconSize(QtCore.QSize(45, 38))
        self.bt_help.setObjectName("bt_help")
        self.horizontalLayout_2.addWidget(self.bt_help)
        self.bt_info = QtWidgets.QPushButton(self.frame_superior)
        self.bt_info.setMinimumSize(QtCore.QSize(50, 50))
        self.bt_info.setStyleSheet("QPushButton{\n"
"border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:rgb(145, 200, 228);\n"
"\n"
"}\n"
"")
        self.bt_info.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_info.setIcon(icon3)
        self.bt_info.setIconSize(QtCore.QSize(45, 38))
        self.bt_info.setObjectName("bt_info")
        self.horizontalLayout_2.addWidget(self.bt_info)
        self.bt_closesesion = QtWidgets.QPushButton(self.frame_superior)
        self.bt_closesesion.setStyleSheet("QPushButton{\n"
"border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:rgb(145, 200, 228);\n"
"\n"
"}\n"
"")
        self.bt_closesesion.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/close-filled(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_closesesion.setIcon(icon4)
        self.bt_closesesion.setIconSize(QtCore.QSize(45, 38))
        self.bt_closesesion.setObjectName("bt_closesesion")
        self.horizontalLayout_2.addWidget(self.bt_closesesion)
        self.bt_salir = QtWidgets.QPushButton(self.frame_superior)
        self.bt_salir.setMinimumSize(QtCore.QSize(50, 50))
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/exit-fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_salir.setIcon(icon5)
        self.bt_salir.setIconSize(QtCore.QSize(45, 38))
        self.bt_salir.setObjectName("bt_salir")
        self.horizontalLayout_2.addWidget(self.bt_salir)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frame_superior)
        self.frame_contenido = QtWidgets.QFrame(self.frame)
        self.frame_contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contenido.setObjectName("frame_contenido")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_contenido)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_opciones = QtWidgets.QFrame(self.frame_contenido)
        self.frame_opciones.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_opciones.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_opciones.setStyleSheet("QFrame{\n"
"background-color:rgb(246, 244, 235);\n"
"border-radius:25px;\n"
"}\n"
"")
        self.frame_opciones.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_opciones.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_opciones.setObjectName("frame_opciones")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_opciones)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.frame_opciones)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.bt_home = QtWidgets.QPushButton(self.frame_opciones)
        self.bt_home.setMinimumSize(QtCore.QSize(50, 50))
        self.bt_home.setStyleSheet("QPushButton{\n"
"border-radius:25px;\n"
"background-color:rgb(246, 244, 235);\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:rgb(145, 200, 228);\n"
"\n"
"}")
        self.bt_home.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/casa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_home.setIcon(icon6)
        self.bt_home.setIconSize(QtCore.QSize(45, 45))
        self.bt_home.setObjectName("bt_home")
        self.verticalLayout_3.addWidget(self.bt_home)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.label_6 = QtWidgets.QLabel(self.frame_opciones)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.bt_registro = QtWidgets.QPushButton(self.frame_opciones)
        self.bt_registro.setMinimumSize(QtCore.QSize(50, 50))
        self.bt_registro.setStyleSheet("QPushButton{\n"
"border-radius:25px;\n"
"background-color:rgb(246, 244, 235);\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:rgb(145, 200, 228);\n"
"\n"
"}\n"
"")
        self.bt_registro.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/registro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_registro.setIcon(icon7)
        self.bt_registro.setIconSize(QtCore.QSize(45, 45))
        self.bt_registro.setObjectName("bt_registro")
        self.verticalLayout_3.addWidget(self.bt_registro)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.label_7 = QtWidgets.QLabel(self.frame_opciones)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.bt_paciente = QtWidgets.QPushButton(self.frame_opciones)
        self.bt_paciente.setMinimumSize(QtCore.QSize(50, 50))
        self.bt_paciente.setStyleSheet("QPushButton{\n"
"border-radius:25px;\n"
"background-color:rgb(246, 244, 235);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:rgb(145, 200, 228);\n"
"\n"
"}\n"
"")
        self.bt_paciente.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/radiografia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_paciente.setIcon(icon8)
        self.bt_paciente.setIconSize(QtCore.QSize(45, 45))
        self.bt_paciente.setObjectName("bt_paciente")
        self.verticalLayout_3.addWidget(self.bt_paciente)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.label_8 = QtWidgets.QLabel(self.frame_opciones)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.bt_citas = QtWidgets.QPushButton(self.frame_opciones)
        self.bt_citas.setMinimumSize(QtCore.QSize(50, 50))
        self.bt_citas.setStyleSheet("QPushButton{\n"
"border-radius:25px;\n"
"background-color:rgb(246, 244, 235);\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:rgb(145, 200, 228);\n"
"\n"
"}\n"
"")
        self.bt_citas.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/cita-dental.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_citas.setIcon(icon9)
        self.bt_citas.setIconSize(QtCore.QSize(45, 45))
        self.bt_citas.setObjectName("bt_citas")
        self.verticalLayout_3.addWidget(self.bt_citas)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.label_9 = QtWidgets.QLabel(self.frame_opciones)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.bt_historial = QtWidgets.QPushButton(self.frame_opciones)
        self.bt_historial.setMinimumSize(QtCore.QSize(50, 50))
        self.bt_historial.setStyleSheet("QPushButton{\n"
"border-radius:25px;\n"
"background-color:rgb(246, 244, 235);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:rgb(145, 200, 228);\n"
"\n"
"}\n"
"")
        self.bt_historial.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/sharp-update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_historial.setIcon(icon10)
        self.bt_historial.setIconSize(QtCore.QSize(45, 45))
        self.bt_historial.setObjectName("bt_historial")
        self.verticalLayout_3.addWidget(self.bt_historial)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.label_15 = QtWidgets.QLabel(self.frame_opciones)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.bt_montos = QtWidgets.QPushButton(self.frame_opciones)
        self.bt_montos.setMinimumSize(QtCore.QSize(50, 50))
        self.bt_montos.setStyleSheet("QPushButton{\n"
"border-radius:25px;\n"
"background-color:rgb(246, 244, 235);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:rgb(145, 200, 228);\n"
"\n"
"}\n"
"")
        self.bt_montos.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/cesar.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_montos.setIcon(icon11)
        self.bt_montos.setIconSize(QtCore.QSize(45, 45))
        self.bt_montos.setObjectName("bt_montos")
        self.verticalLayout_3.addWidget(self.bt_montos)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.frame_opciones)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lb_nombre = QtWidgets.QLabel(self.frame_contenido)
        self.lb_nombre.setMinimumSize(QtCore.QSize(0, 40))
        self.lb_nombre.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lb_nombre.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_nombre.setStyleSheet("QLabel{\n"
"font: 75 italic 18px \"Hack Nerd Font\";\n"
"}")
        self.lb_nombre.setText("")
        self.lb_nombre.setTextFormat(QtCore.Qt.AutoText)
        self.lb_nombre.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_nombre.setObjectName("lb_nombre")
        self.verticalLayout_4.addWidget(self.lb_nombre)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_contenido)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.principal_tab = QtWidgets.QWidget()
        self.principal_tab.setObjectName("principal_tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.principal_tab)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frmae_fondo = QtWidgets.QFrame(self.principal_tab)
        self.frmae_fondo.setStyleSheet("QLabel{\n"
"    font: 12pt \"MS Reference Sans Serif\";\n"
"}\n"
"QFrame{\n"
"    background-color:rgb(0, 85, 127);\n"
"}")
        self.frmae_fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmae_fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmae_fondo.setObjectName("frmae_fondo")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frmae_fondo)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.line_2 = QtWidgets.QFrame(self.frmae_fondo)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_12.addWidget(self.line_2)
        self.label_3 = QtWidgets.QLabel(self.frmae_fondo)
        self.label_3.setMinimumSize(QtCore.QSize(625, 200))
        self.label_3.setMaximumSize(QtCore.QSize(625, 200))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_12.addWidget(self.label_3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 213, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem9)
        self.line_6 = QtWidgets.QFrame(self.frmae_fondo)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_12.addWidget(self.line_6)
        self.frame_2 = QtWidgets.QFrame(self.frmae_fondo)
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color:white;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_11.addWidget(self.label_4)
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_11.addWidget(self.label_12)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_10.addWidget(self.label_5)
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_10.addWidget(self.label_13)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_6.addWidget(self.label_14)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_12.addWidget(self.frame_2)
        self.line = QtWidgets.QFrame(self.frmae_fondo)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_12.addWidget(self.line)
        self.verticalLayout_8.addWidget(self.frmae_fondo)
        self.tabWidget.addTab(self.principal_tab, "")
        self.citas_tab = QtWidgets.QWidget()
        self.citas_tab.setObjectName("citas_tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.citas_tab)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_fondo = QtWidgets.QFrame(self.citas_tab)
        self.frame_fondo.setStyleSheet("QLabel{\n"
"    font: 12pt \"MS Reference Sans Serif\";\n"
"}\n"
"QFrame{\n"
"background-color:rgb(0, 85, 127);\n"
"}")
        self.frame_fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_fondo.setObjectName("frame_fondo")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_fondo)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.line_5 = QtWidgets.QFrame(self.frame_fondo)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_13.addWidget(self.line_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_fondo)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.filtro = QtWidgets.QComboBox(self.frame_fondo)
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
        self.horizontalLayout_5.addWidget(self.filtro)
        self.in_buscar = QtWidgets.QLineEdit(self.frame_fondo)
        self.in_buscar.setMinimumSize(QtCore.QSize(200, 40))
        self.in_buscar.setMaximumSize(QtCore.QSize(200, 40))
        self.in_buscar.setInputMask("")
        self.in_buscar.setText("")
        self.in_buscar.setMaxLength(20)
        self.in_buscar.setPlaceholderText("")
        self.in_buscar.setObjectName("in_buscar")
        self.horizontalLayout_5.addWidget(self.in_buscar)
        self.bt_buscar = QtWidgets.QPushButton(self.frame_fondo)
        self.bt_buscar.setMinimumSize(QtCore.QSize(80, 40))
        self.bt_buscar.setMaximumSize(QtCore.QSize(80, 40))
        self.bt_buscar.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/buscar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_buscar.setIcon(icon12)
        self.bt_buscar.setIconSize(QtCore.QSize(30, 30))
        self.bt_buscar.setObjectName("bt_buscar")
        self.horizontalLayout_5.addWidget(self.bt_buscar)
        self.verticalLayout_13.addLayout(self.horizontalLayout_5)
        self.line_3 = QtWidgets.QFrame(self.frame_fondo)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_13.addWidget(self.line_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.bt_act = QtWidgets.QPushButton(self.frame_fondo)
        self.bt_act.setMinimumSize(QtCore.QSize(150, 50))
        self.bt_act.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bt_act.setFont(font)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/actualizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_act.setIcon(icon13)
        self.bt_act.setIconSize(QtCore.QSize(30, 30))
        self.bt_act.setObjectName("bt_act")
        self.horizontalLayout_7.addWidget(self.bt_act)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.verticalLayout_13.addLayout(self.horizontalLayout_7)
        self.frame_tabla = QtWidgets.QFrame(self.frame_fondo)
        self.frame_tabla.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_tabla.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tabla.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tabla.setObjectName("frame_tabla")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_tabla)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tabla_cita = QtWidgets.QTableWidget(self.frame_tabla)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabla_cita.setFont(font)
        self.tabla_cita.setObjectName("tabla_cita")
        self.tabla_cita.setColumnCount(6)
        self.tabla_cita.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_cita.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_cita.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_cita.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_cita.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_cita.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_cita.setHorizontalHeaderItem(5, item)
        self.tabla_cita.horizontalHeader().setDefaultSectionSize(237)
        self.tabla_cita.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_9.addWidget(self.tabla_cita)
        self.verticalLayout_13.addWidget(self.frame_tabla)
        self.line_4 = QtWidgets.QFrame(self.frame_fondo)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_13.addWidget(self.line_4)
        self.verticalLayout_7.addWidget(self.frame_fondo)
        self.tabWidget.addTab(self.citas_tab, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addWidget(self.frame_contenido)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Menu principal"))
        self.label.setText(_translate("MainWindow", "Home"))
        self.label_6.setText(_translate("MainWindow", "Registro de pacientes"))
        self.label_7.setText(_translate("MainWindow", "Placas dentales"))
        self.label_8.setText(_translate("MainWindow", "Agendar citas"))
        self.label_9.setText(_translate("MainWindow", "Generar historias"))
        self.label_15.setText(_translate("MainWindow", "Cambiar montos de tratamientos"))
        self.label_3.setText(_translate("MainWindow", "Logo del consultorio"))
        self.label_4.setText(_translate("MainWindow", "Direccion"))
        self.label_12.setText(_translate("MainWindow", "Direccion"))
        self.label_5.setText(_translate("MainWindow", "Numero de contacto"))
        self.label_13.setText(_translate("MainWindow", "Numero de contacto"))
        self.label_11.setText(_translate("MainWindow", "X"))
        self.label_14.setText(_translate("MainWindow", "X"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.principal_tab), _translate("MainWindow", "Pagina principal"))
        self.label_2.setText(_translate("MainWindow", "Pacientes con citas más cercanas"))
        self.bt_act.setText(_translate("MainWindow", "Actualizar tabla"))
        item = self.tabla_cita.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Cedula"))
        item = self.tabla_cita.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tabla_cita.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Apellido"))
        item = self.tabla_cita.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.tabla_cita.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Hora"))
        item = self.tabla_cita.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Estatus de cita"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.citas_tab), _translate("MainWindow", "Citas proximas"))
