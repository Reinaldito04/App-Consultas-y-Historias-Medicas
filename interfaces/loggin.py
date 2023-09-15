from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.contenedorP = QtWidgets.QFrame(self.centralwidget)
        self.contenedorP.setAutoFillBackground(False)
        self.contenedorP.setStyleSheet("QFrame{\n"
"background-color:black;\n"
"}")
        self.contenedorP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contenedorP.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contenedorP.setObjectName("contenedorP")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.contenedorP)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_contenido = QtWidgets.QFrame(self.contenedorP)
        self.frame_contenido.setStyleSheet("QFrame{\n"
"background-color:gray;\n"
"}")
        self.frame_contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contenido.setObjectName("frame_contenido")
        self.frame = QtWidgets.QFrame(self.frame_contenido)
        self.frame.setGeometry(QtCore.QRect(170, 50, 471, 441))
        self.frame.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(255, 255, 0);\n"
"border-radius:40px;\n"
"    background-color: rgb(170, 85, 127);\n"
"font:16pt \"SansSerif\"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 127);\n"
"}\n"
"QLabel{\n"
"color:black;\n"
"    font: 75 17pt \"Times New Roman\";\n"
"\n"
"}\n"
"QLineEdit{\n"
"border-radius:12px;\n"
"font:14pt \"SansSerif\";\n"
"border:2px solid rgb(0, 0, 0);\n"
"color:black;\n"
"}\n"
"QLineEdit:hover{\n"
"border-radius:12px;\n"
"font:10pt \"SansSerif\";\n"
"border:2px solid rgb(255, 0, 0);\n"
"color:black;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(80, 60, 315, 242))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QLabel(self.widget)
        self.title.setStyleSheet("QLabel{\n"
"font:24pt \"SansSerif\"\n"
"}")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title)
        self.user_label = QtWidgets.QLabel(self.widget)
        self.user_label.setAlignment(QtCore.Qt.AlignCenter)
        self.user_label.setObjectName("user_label")
        self.verticalLayout_2.addWidget(self.user_label)
        self.in_password = QtWidgets.QLineEdit(self.widget)
        self.in_password.setText("")
        self.in_password.setObjectName("in_password")
        self.verticalLayout_2.addWidget(self.in_password)
        self.password_label = QtWidgets.QLabel(self.widget)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.verticalLayout_2.addWidget(self.password_label)
        self.in_user = QtWidgets.QLineEdit(self.widget)
        self.in_user.setText("")
        self.in_user.setObjectName("in_user")
        self.verticalLayout_2.addWidget(self.in_user)
        self.espacio = QtWidgets.QLabel(self.widget)
        self.espacio.setText("")
        self.espacio.setObjectName("espacio")
        self.verticalLayout_2.addWidget(self.espacio)
        self.btn_in = QtWidgets.QPushButton(self.widget)
        self.btn_in.setObjectName("btn_in")
        self.verticalLayout_2.addWidget(self.btn_in)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout_2.setStretch(4, 2)
        self.verticalLayout_2.setStretch(6, 2)
        self.widget1 = QtWidgets.QWidget(self.frame)
        self.widget1.setGeometry(QtCore.QRect(10, 380, 441, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setStyleSheet("QLabel{\n"
"font:12pt \"SansSerif\"\n"
"}")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame_contenido)
        self.horizontalLayout.addWidget(self.contenedorP)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "INICIO DE SESION"))
        self.user_label.setText(_translate("MainWindow", "Usuario:"))
        self.password_label.setText(_translate("MainWindow", "Contraseña:"))
        self.btn_in.setText(_translate("MainWindow", "INGRESAR"))
        self.label_4.setText(_translate("MainWindow", "Si no esta registrado, pulse en \"Registrar\""))
        self.pushButton_2.setText(_translate("MainWindow", "REGISTRAR"))
        
    def validar_ingreso(self):
        usuario = self.in_user.text()
        contrasena = self.in_password.text()

        if len(usuario) < 6:
            QtWidgets.QMessageBox.critical(
                None,
                "Error de usuario",
                "El usuario debe tener al menos 6 caracteres.",
                QtWidgets.QMessageBox.Ok,
            )
            return

        if len(contrasena) < 8:
            QtWidgets.QMessageBox.critical(
                None,
                "Error de contraseña",
                "La contraseña debe tener al menos 8 caracteres.",
                QtWidgets.QMessageBox.Ok,
            )
            return
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() 
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())