# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/montos.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_montos(object):
    def setupUi(self, montos):
        montos.setObjectName("montos")
        montos.resize(1046, 473)
        self.centralwidget = QtWidgets.QWidget(montos)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"background-color:gray;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color:#138D75;\n"
"    font: 12pt \"Microsoft Sans Serif\";\n"
"}\n"
"QTableWidget{\n"
"color:rgb(0,0,0);\n"
"gridline-color:rgb(0,206,151);\n"
"font-size:12pt;\n"
"}\n"
"QHeaderView::section{\n"
"background-color:rgb(0,206,151);\n"
"border:1px solid rgb(0,0,0);\n"
"font-size:12pt;\n"
"}\n"
"QTbaleWidget QTableCornerButton::section{\n"
"background-color:rgb(0,0,0);\n"
"border:1px solid  rgb(0,206,151);\n"
"}\n"
"QLineEdit{\n"
"border-radius:19px;\n"
"border:2px solid rgb(0,0,0);\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 12pt \"Microsoft Sans Serif\";\n"
"}\n"
"QPushButton{\n"
"border-radius:20px;\n"
"border:2px solid rgb(0,0,0);\n"
"background-color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#CB4335;\n"
"}\n"
"QTextEdit{\n"
"border:4px solid rgb(0,0,0);\n"
"border-radius:20px;\n"
"    font: 12pt \"Microsoft Sans Serif\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox{\n"
"border:2px solid rgb(0,0,0);\n"
"    font: 12pt \"Microsoft Sans Serif\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.t_0 = QtWidgets.QComboBox(self.frame_2)
        self.t_0.setMinimumSize(QtCore.QSize(300, 40))
        self.t_0.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.t_0.setFont(font)
        self.t_0.setEditable(False)
        self.t_0.setCurrentText("")
        self.t_0.setMaxVisibleItems(20)
        self.t_0.setObjectName("t_0")
        self.horizontalLayout_7.addWidget(self.t_0)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.t_1 = QtWidgets.QLineEdit(self.frame_2)
        self.t_1.setMinimumSize(QtCore.QSize(400, 40))
        self.t_1.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.t_1.setFont(font)
        self.t_1.setAlignment(QtCore.Qt.AlignCenter)
        self.t_1.setReadOnly(True)
        self.t_1.setObjectName("t_1")
        self.verticalLayout_4.addWidget(self.t_1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.monto_1 = QtWidgets.QLineEdit(self.frame_2)
        self.monto_1.setMinimumSize(QtCore.QSize(180, 40))
        self.monto_1.setMaximumSize(QtCore.QSize(180, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.monto_1.setFont(font)
        self.monto_1.setStyleSheet("font-size:14px;")
        self.monto_1.setMaxLength(4)
        self.monto_1.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_1.setReadOnly(False)
        self.monto_1.setObjectName("monto_1")
        self.horizontalLayout.addWidget(self.monto_1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.t_2 = QtWidgets.QLineEdit(self.frame_2)
        self.t_2.setMinimumSize(QtCore.QSize(400, 40))
        self.t_2.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.t_2.setFont(font)
        self.t_2.setAlignment(QtCore.Qt.AlignCenter)
        self.t_2.setReadOnly(True)
        self.t_2.setObjectName("t_2")
        self.verticalLayout_5.addWidget(self.t_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.monto_2 = QtWidgets.QLineEdit(self.frame_2)
        self.monto_2.setMinimumSize(QtCore.QSize(180, 40))
        self.monto_2.setMaximumSize(QtCore.QSize(180, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.monto_2.setFont(font)
        self.monto_2.setStyleSheet("font-size:14px;")
        self.monto_2.setMaxLength(4)
        self.monto_2.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_2.setReadOnly(False)
        self.monto_2.setObjectName("monto_2")
        self.horizontalLayout_2.addWidget(self.monto_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem8)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.t_3 = QtWidgets.QLineEdit(self.frame_2)
        self.t_3.setMinimumSize(QtCore.QSize(400, 40))
        self.t_3.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.t_3.setFont(font)
        self.t_3.setAlignment(QtCore.Qt.AlignCenter)
        self.t_3.setReadOnly(True)
        self.t_3.setObjectName("t_3")
        self.verticalLayout_6.addWidget(self.t_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.monto_3 = QtWidgets.QLineEdit(self.frame_2)
        self.monto_3.setMinimumSize(QtCore.QSize(180, 40))
        self.monto_3.setMaximumSize(QtCore.QSize(180, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.monto_3.setFont(font)
        self.monto_3.setStyleSheet("font-size:14px;")
        self.monto_3.setMaxLength(4)
        self.monto_3.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_3.setReadOnly(False)
        self.monto_3.setObjectName("monto_3")
        self.horizontalLayout_3.addWidget(self.monto_3)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_8.addLayout(self.verticalLayout_7)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.t_4 = QtWidgets.QLineEdit(self.frame_2)
        self.t_4.setMinimumSize(QtCore.QSize(400, 40))
        self.t_4.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.t_4.setFont(font)
        self.t_4.setAlignment(QtCore.Qt.AlignCenter)
        self.t_4.setReadOnly(True)
        self.t_4.setObjectName("t_4")
        self.verticalLayout_8.addWidget(self.t_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.monto_4 = QtWidgets.QLineEdit(self.frame_2)
        self.monto_4.setMinimumSize(QtCore.QSize(180, 40))
        self.monto_4.setMaximumSize(QtCore.QSize(180, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.monto_4.setFont(font)
        self.monto_4.setStyleSheet("font-size:14px;")
        self.monto_4.setMaxLength(4)
        self.monto_4.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_4.setReadOnly(False)
        self.monto_4.setObjectName("monto_4")
        self.horizontalLayout_6.addWidget(self.monto_4)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout_11.addLayout(self.verticalLayout_8)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem14)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.t_5 = QtWidgets.QLineEdit(self.frame_2)
        self.t_5.setMinimumSize(QtCore.QSize(400, 40))
        self.t_5.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.t_5.setFont(font)
        self.t_5.setAlignment(QtCore.Qt.AlignCenter)
        self.t_5.setReadOnly(True)
        self.t_5.setObjectName("t_5")
        self.verticalLayout_9.addWidget(self.t_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.monto_5 = QtWidgets.QLineEdit(self.frame_2)
        self.monto_5.setMinimumSize(QtCore.QSize(180, 40))
        self.monto_5.setMaximumSize(QtCore.QSize(180, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.monto_5.setFont(font)
        self.monto_5.setStyleSheet("font-size:14px;")
        self.monto_5.setMaxLength(4)
        self.monto_5.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_5.setReadOnly(False)
        self.monto_5.setObjectName("monto_5")
        self.horizontalLayout_5.addWidget(self.monto_5)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem16)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.verticalLayout_11.addLayout(self.verticalLayout_9)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem17)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.t_6 = QtWidgets.QLineEdit(self.frame_2)
        self.t_6.setMinimumSize(QtCore.QSize(400, 40))
        self.t_6.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.t_6.setFont(font)
        self.t_6.setAlignment(QtCore.Qt.AlignCenter)
        self.t_6.setReadOnly(True)
        self.t_6.setObjectName("t_6")
        self.verticalLayout_10.addWidget(self.t_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem18)
        self.monto_6 = QtWidgets.QLineEdit(self.frame_2)
        self.monto_6.setMinimumSize(QtCore.QSize(180, 40))
        self.monto_6.setMaximumSize(QtCore.QSize(180, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.monto_6.setFont(font)
        self.monto_6.setStyleSheet("font-size:14px;")
        self.monto_6.setMaxLength(4)
        self.monto_6.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_6.setReadOnly(False)
        self.monto_6.setObjectName("monto_6")
        self.horizontalLayout_4.addWidget(self.monto_6)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem19)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.horizontalLayout_8.addLayout(self.verticalLayout_11)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9.addLayout(self.verticalLayout_12)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem20)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setStyleSheet("QLabel{\n"
"background-color:white;\n"
"border-right:2px solid rgb(0,0,0);\n"
"border-left:2px solid rgb(0,0,0);\n"
"border-top:2px solid rgb(0,0,0);\n"
"}")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_30.addWidget(self.label_11)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setStyleSheet("QFrame{\n"
"    background-color:rgb(70, 130, 169);\n"
"border-right:2px solid rgb(0,0,0);\n"
"border-left:2px solid rgb(0,0,0);\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"border-top:2px solid rgb(0,0,0);\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_52 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.verticalLayout_62 = QtWidgets.QVBoxLayout()
        self.verticalLayout_62.setObjectName("verticalLayout_62")
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_62.addItem(spacerItem21)
        self.btn_agg = QtWidgets.QPushButton(self.frame_9)
        self.btn_agg.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_agg.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_agg.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_agg.setIcon(icon)
        self.btn_agg.setIconSize(QtCore.QSize(25, 25))
        self.btn_agg.setObjectName("btn_agg")
        self.verticalLayout_62.addWidget(self.btn_agg)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_62.addItem(spacerItem22)
        self.btn_clear = QtWidgets.QPushButton(self.frame_9)
        self.btn_clear.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_clear.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_clear.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/ELEMENTOS GRAFICOS/limpiar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_clear.setIcon(icon1)
        self.btn_clear.setIconSize(QtCore.QSize(25, 25))
        self.btn_clear.setObjectName("btn_clear")
        self.verticalLayout_62.addWidget(self.btn_clear)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_62.addItem(spacerItem23)
        self.verticalLayout_52.addLayout(self.verticalLayout_62)
        self.verticalLayout_30.addWidget(self.frame_9)
        self.verticalLayout_13.addLayout(self.verticalLayout_30)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem24)
        self.horizontalLayout_9.addLayout(self.verticalLayout_13)
        self.verticalLayout_14.addLayout(self.horizontalLayout_9)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem25)
        self.horizontalLayout_10.addLayout(self.verticalLayout_14)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.frame)
        montos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(montos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1046, 20))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        montos.setMenuBar(self.menubar)
        self.actionSalir = QtWidgets.QAction(montos)
        self.actionSalir.setObjectName("actionSalir")
        self.actionRegresar_al_menu_prinicipal = QtWidgets.QAction(montos)
        self.actionRegresar_al_menu_prinicipal.setObjectName("actionRegresar_al_menu_prinicipal")
        self.menuMenu.addAction(self.actionRegresar_al_menu_prinicipal)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionSalir)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(montos)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(montos)

    def retranslateUi(self, montos):
        _translate = QtCore.QCoreApplication.translate
        montos.setWindowTitle(_translate("montos", "MainWindow"))
        self.t_1.setPlaceholderText(_translate("montos", "Tratamiento 1"))
        self.monto_1.setPlaceholderText(_translate("montos", "Ingrese el monto en $$$"))
        self.t_2.setPlaceholderText(_translate("montos", "Tratamiento 2"))
        self.monto_2.setPlaceholderText(_translate("montos", "Ingrese el monto en $$$"))
        self.t_3.setPlaceholderText(_translate("montos", "Tratamiento 3"))
        self.monto_3.setPlaceholderText(_translate("montos", "Ingrese el monto en $$$"))
        self.t_4.setPlaceholderText(_translate("montos", "Tratamiento 4"))
        self.monto_4.setPlaceholderText(_translate("montos", "Ingrese el monto en $$$"))
        self.t_5.setPlaceholderText(_translate("montos", "Tratamiento 5"))
        self.monto_5.setPlaceholderText(_translate("montos", "Ingrese el monto en $$$"))
        self.t_6.setPlaceholderText(_translate("montos", "Tratamiento 6"))
        self.monto_6.setPlaceholderText(_translate("montos", "Ingrese el monto en $$$"))
        self.label_11.setText(_translate("montos", "Controles"))
        self.btn_agg.setText(_translate("montos", "Agregar"))
        self.btn_clear.setText(_translate("montos", "Limpiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("montos", "Montos de tratamientos"))
        self.menuMenu.setTitle(_translate("montos", "Menu"))
        self.actionSalir.setText(_translate("montos", "Salir"))
        self.actionRegresar_al_menu_prinicipal.setText(_translate("montos", "Regresar al menu prinicipal"))
