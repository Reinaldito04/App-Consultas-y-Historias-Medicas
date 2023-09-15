import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget ,QApplication ,QMainWindow,QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QMessageBox,QLabel
import hashlib
import sqlite3


class Registro(QMainWindow):
    def __init__(self):
        super(Registro , self). __init__()
        loadUi("./interfaces/register.ui", self)
        self.bt_end.clicked.connect(self.close)
        self.bt_register.clicked.connect(self.registrarUsuario)
        
    def cifrar_contrasenia(self, contrasenia):
        # Cifrar la contraseña usando un algoritmo de hash (SHA-256 en este caso)
        cifrado = hashlib.sha256()
        cifrado.update(contrasenia.encode('utf-8'))
        return cifrado.hexdigest()
    
    def usuario_existe(self, nombre):
        # Conectar a la base de datos
        conexion = sqlite3.connect('interfaces/database.db')

        # Crear un cursor
        cursor = conexion.cursor()

        # Consultar si el usuario ya existe
        cursor.execute('SELECT COUNT(*) FROM Users WHERE Username = ?', (nombre,))
        resultado = cursor.fetchone()[0]

        # Cerrar la conexión
        conexion.close()

        # Si resultado es mayor que 0, significa que el usuario ya existe
        return resultado > 0
    
    
    def registrarUsuario(self):
        conexion = sqlite3.connect('interfaces\database.db')
        nombre = self.txt_user.text()
        password = self.txt_password.text()
        passwordRepeat = self.txt_password_repeat.text()
        
        if len(nombre and password and passwordRepeat) <=0:
            QMessageBox.critical(self,"Error","Ningun campo ha sido llenado")
        else :
            if len(nombre) != 4:
                QMessageBox.critical(self, "Error", "El nombre de usuario debe tener 4 caracteres.")
        
            if len(password) != 4:
             QMessageBox.critical(self, "Error", "La contraseña debe tener 8 caracteres.")
            if len(passwordRepeat) != 4:
                QMessageBox.critical(self, "Error", "La contraseña debe tener 8 caracteres.")
        
         
        if password == passwordRepeat:
            if self.usuario_existe(nombre):
                QMessageBox.warning(self, "Error", "El nombre de usuario ya existe. \nIngrese uno distinto")
            else:
                # Conectar a la base de datos
                contrasenia_cifrada = self.cifrar_contrasenia(password)
                conexion = sqlite3.connect('interfaces/database.db')

                # Crear un cursor
                cursor = conexion.cursor()

                # Insertar datos en la base de datos
                cursor.execute('INSERT INTO Users (Username, Password) VALUES (?, ?)', (nombre, contrasenia_cifrada))

                # Confirmar los cambios en la base de datos y cerrar la conexión
                conexion.commit()
                conexion.close()

                QMessageBox.information(self, "Éxito", "Registro exitoso")
        else:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden")
            self.txt_user.clear()
            self.txt_password.clear()
            self.txt_password_repeat.clear()
       

        
        
        
    def close(self):
       QApplication.quit()
        
        
app = QApplication(sys.argv)
Registro = Registro()
widget = QtWidgets.QStackedWidget()
widget.addWidget(Registro)
widget.move(200, 80)
widget.setFixedHeight(1000)
widget.setFixedWidth(1000)
widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
widget.show()



try:
    sys.exit(app.exec_())
except:
    print("saliendo")