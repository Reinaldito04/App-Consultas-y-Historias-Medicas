# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/SI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SI(object):
    def setupUi(self, SI):
        SI.setObjectName("SI")
        SI.resize(696, 491)
        self.centralwidget = QtWidgets.QWidget(SI)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        self.c_0 = QtWidgets.QComboBox(self.frame)
        self.c_0.setMinimumSize(QtCore.QSize(300, 30))
        self.c_0.setObjectName("c_0")
        self.horizontalLayout_12.addWidget(self.c_0)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.t_0 = QtWidgets.QComboBox(self.frame)
        self.t_0.setMinimumSize(QtCore.QSize(300, 30))
        self.t_0.setObjectName("t_0")
        self.horizontalLayout_11.addWidget(self.t_0)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.monto_bs_1 = QtWidgets.QLineEdit(self.frame)
        self.monto_bs_1.setMinimumSize(QtCore.QSize(90, 30))
        self.monto_bs_1.setMaximumSize(QtCore.QSize(90, 30))
        self.monto_bs_1.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_bs_1.setReadOnly(True)
        self.monto_bs_1.setObjectName("monto_bs_1")
        self.horizontalLayout.addWidget(self.monto_bs_1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.monto_dola_1 = QtWidgets.QLineEdit(self.frame)
        self.monto_dola_1.setMinimumSize(QtCore.QSize(90, 30))
        self.monto_dola_1.setMaximumSize(QtCore.QSize(90, 30))
        self.monto_dola_1.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_dola_1.setReadOnly(True)
        self.monto_dola_1.setObjectName("monto_dola_1")
        self.horizontalLayout.addWidget(self.monto_dola_1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem12)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem13)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem14)
        self.c_2 = QtWidgets.QComboBox(self.frame)
        self.c_2.setMinimumSize(QtCore.QSize(300, 30))
        self.c_2.setObjectName("c_2")
        self.horizontalLayout_15.addWidget(self.c_2)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem15)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem16)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem17)
        self.t_2 = QtWidgets.QComboBox(self.frame)
        self.t_2.setMinimumSize(QtCore.QSize(300, 30))
        self.t_2.setObjectName("t_2")
        self.horizontalLayout_16.addWidget(self.t_2)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem18)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem19)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem20)
        self.monto_bs_3 = QtWidgets.QLineEdit(self.frame)
        self.monto_bs_3.setMinimumSize(QtCore.QSize(90, 30))
        self.monto_bs_3.setMaximumSize(QtCore.QSize(90, 30))
        self.monto_bs_3.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_bs_3.setReadOnly(True)
        self.monto_bs_3.setObjectName("monto_bs_3")
        self.horizontalLayout_3.addWidget(self.monto_bs_3)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem21)
        self.monto_dola_3 = QtWidgets.QLineEdit(self.frame)
        self.monto_dola_3.setMinimumSize(QtCore.QSize(90, 30))
        self.monto_dola_3.setMaximumSize(QtCore.QSize(90, 30))
        self.monto_dola_3.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_dola_3.setReadOnly(True)
        self.monto_dola_3.setObjectName("monto_dola_3")
        self.horizontalLayout_3.addWidget(self.monto_dola_3)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem22)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem23)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem24)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem25)
        self.c_4 = QtWidgets.QComboBox(self.frame)
        self.c_4.setMinimumSize(QtCore.QSize(300, 30))
        self.c_4.setObjectName("c_4")
        self.horizontalLayout_19.addWidget(self.c_4)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem26)
        self.verticalLayout_5.addLayout(self.horizontalLayout_19)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem27)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem28)
        self.t_4 = QtWidgets.QComboBox(self.frame)
        self.t_4.setMinimumSize(QtCore.QSize(300, 30))
        self.t_4.setObjectName("t_4")
        self.horizontalLayout_20.addWidget(self.t_4)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem29)
        self.verticalLayout_5.addLayout(self.horizontalLayout_20)
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem30)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem31)
        self.monto_bs_5 = QtWidgets.QLineEdit(self.frame)
        self.monto_bs_5.setMinimumSize(QtCore.QSize(90, 30))
        self.monto_bs_5.setMaximumSize(QtCore.QSize(90, 30))
        self.monto_bs_5.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_bs_5.setReadOnly(True)
        self.monto_bs_5.setObjectName("monto_bs_5")
        self.horizontalLayout_5.addWidget(self.monto_bs_5)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem32)
        self.monto_dola_5 = QtWidgets.QLineEdit(self.frame)
        self.monto_dola_5.setMinimumSize(QtCore.QSize(90, 30))
        self.monto_dola_5.setMaximumSize(QtCore.QSize(90, 30))
        self.monto_dola_5.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_dola_5.setReadOnly(True)
        self.monto_dola_5.setObjectName("monto_dola_5")
        self.horizontalLayout_5.addWidget(self.monto_dola_5)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem33)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        spacerItem34 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem34)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem35 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem35)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem36)
        self.c_1 = QtWidgets.QComboBox(self.frame)
        self.c_1.setMinimumSize(QtCore.QSize(300, 30))
        self.c_1.setObjectName("c_1")
        self.horizontalLayout_13.addWidget(self.c_1)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem37)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        spacerItem38 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem38)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem39)
        self.t_1 = QtWidgets.QComboBox(self.frame)
        self.t_1.setMinimumSize(QtCore.QSize(300, 30))
        self.t_1.setObjectName("t_1")
        self.horizontalLayout_14.addWidget(self.t_1)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem40)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        spacerItem41 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem41)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem42 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem42)
        self.monto_bs_2 = QtWidgets.QLineEdit(self.frame)
        self.monto_bs_2.setMinimumSize(QtCore.QSize(90, 30))
        self.monto_bs_2.setMaximumSize(QtCore.QSize(90, 30))
        self.monto_bs_2.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_bs_2.setReadOnly(True)
        self.monto_bs_2.setObjectName("monto_bs_2")
        self.horizontalLayout_2.addWidget(self.monto_bs_2)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem43)
        self.monto_dola_2 = QtWidgets.QLineEdit(self.frame)
        self.monto_dola_2.setMinimumSize(QtCore.QSize(90, 30))
        self.monto_dola_2.setMaximumSize(QtCore.QSize(90, 30))
        self.monto_dola_2.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_dola_2.setReadOnly(True)
        self.monto_dola_2.setObjectName("monto_dola_2")
        self.horizontalLayout_2.addWidget(self.monto_dola_2)
        spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem44)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem45 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem45)
        self.verticalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem46 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem46)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem47 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem47)
        self.c_3 = QtWidgets.QComboBox(self.frame)
        self.c_3.setMinimumSize(QtCore.QSize(300, 30))
        self.c_3.setObjectName("c_3")
        self.horizontalLayout_17.addWidget(self.c_3)
        spacerItem48 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem48)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        spacerItem49 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem49)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem50 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem50)
        self.t_3 = QtWidgets.QComboBox(self.frame)
        self.t_3.setMinimumSize(QtCore.QSize(300, 30))
        self.t_3.setObjectName("t_3")
        self.horizontalLayout_18.addWidget(self.t_3)
        spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem51)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        spacerItem52 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem52)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem53 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem53)
        self.monto_bs_4 = QtWidgets.QLineEdit(self.frame)
        self.monto_bs_4.setMinimumSize(QtCore.QSize(90, 30))
        self.monto_bs_4.setMaximumSize(QtCore.QSize(90, 30))
        self.monto_bs_4.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_bs_4.setReadOnly(True)
        self.monto_bs_4.setObjectName("monto_bs_4")
        self.horizontalLayout_4.addWidget(self.monto_bs_4)
        spacerItem54 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem54)
        self.monto_dola_4 = QtWidgets.QLineEdit(self.frame)
        self.monto_dola_4.setMinimumSize(QtCore.QSize(90, 30))
        self.monto_dola_4.setMaximumSize(QtCore.QSize(90, 30))
        self.monto_dola_4.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_dola_4.setReadOnly(True)
        self.monto_dola_4.setObjectName("monto_dola_4")
        self.horizontalLayout_4.addWidget(self.monto_dola_4)
        spacerItem55 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem55)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem56 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem56)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem57 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem57)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem58 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem58)
        self.c_5 = QtWidgets.QComboBox(self.frame)
        self.c_5.setMinimumSize(QtCore.QSize(300, 30))
        self.c_5.setObjectName("c_5")
        self.horizontalLayout_21.addWidget(self.c_5)
        spacerItem59 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem59)
        self.verticalLayout_6.addLayout(self.horizontalLayout_21)
        spacerItem60 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem60)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        spacerItem61 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem61)
        self.t_5 = QtWidgets.QComboBox(self.frame)
        self.t_5.setMinimumSize(QtCore.QSize(300, 30))
        self.t_5.setObjectName("t_5")
        self.horizontalLayout_22.addWidget(self.t_5)
        spacerItem62 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem62)
        self.verticalLayout_6.addLayout(self.horizontalLayout_22)
        spacerItem63 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem63)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem64 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem64)
        self.monto_bs_6 = QtWidgets.QLineEdit(self.frame)
        self.monto_bs_6.setMinimumSize(QtCore.QSize(90, 30))
        self.monto_bs_6.setMaximumSize(QtCore.QSize(90, 30))
        self.monto_bs_6.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_bs_6.setReadOnly(True)
        self.monto_bs_6.setObjectName("monto_bs_6")
        self.horizontalLayout_6.addWidget(self.monto_bs_6)
        spacerItem65 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem65)
        self.monto_dola_6 = QtWidgets.QLineEdit(self.frame)
        self.monto_dola_6.setMinimumSize(QtCore.QSize(90, 30))
        self.monto_dola_6.setMaximumSize(QtCore.QSize(90, 30))
        self.monto_dola_6.setAlignment(QtCore.Qt.AlignCenter)
        self.monto_dola_6.setReadOnly(True)
        self.monto_dola_6.setObjectName("monto_dola_6")
        self.horizontalLayout_6.addWidget(self.monto_dola_6)
        spacerItem66 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem66)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        spacerItem67 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem67)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addWidget(self.frame)
        spacerItem68 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem68)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        spacerItem69 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem69)
        SI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 696, 21))
        self.menubar.setObjectName("menubar")
        SI.setMenuBar(self.menubar)

        self.retranslateUi(SI)
        QtCore.QMetaObject.connectSlotsByName(SI)

    def retranslateUi(self, SI):
        _translate = QtCore.QCoreApplication.translate
        SI.setWindowTitle(_translate("SI", "MainWindow"))
        self.monto_bs_1.setPlaceholderText(_translate("SI", "Monto en Bs."))
        self.monto_dola_1.setPlaceholderText(_translate("SI", "Monto en $$$"))
        self.monto_bs_3.setPlaceholderText(_translate("SI", "Monto en Bs."))
        self.monto_dola_3.setPlaceholderText(_translate("SI", "Monto en $$$"))
        self.monto_bs_5.setPlaceholderText(_translate("SI", "Monto en Bs."))
        self.monto_dola_5.setPlaceholderText(_translate("SI", "Monto en $$$"))
        self.monto_bs_2.setPlaceholderText(_translate("SI", "Monto en Bs."))
        self.monto_dola_2.setPlaceholderText(_translate("SI", "Monto en $$$"))
        self.monto_bs_4.setPlaceholderText(_translate("SI", "Monto en Bs."))
        self.monto_dola_4.setPlaceholderText(_translate("SI", "Monto en $$$"))
        self.monto_bs_6.setPlaceholderText(_translate("SI", "Monto en Bs."))
        self.monto_dola_6.setPlaceholderText(_translate("SI", "Monto en $$$"))