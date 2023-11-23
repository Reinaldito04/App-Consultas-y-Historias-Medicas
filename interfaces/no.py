import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QBuffer, QByteArray, QIODevice
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDialog
import hashlib
import sqlite3
import re
from users import Ui_Dialog

class Registro(QtWidgets.QMainWindow):
    def __init__(self):
        super(Registro, self).__init__()
        loadUi("interfaces/dogtores.ui", self)
        self.btn_agg.clicked.connect(self.registrarUsuario)
        self.btn_clear.clicked.connect(self.clearInputs)
        self.actionSalir.triggered.connect(self.close)
        self.bt_photo.clicked.connect(self.addPhoto)
        self.in_cedula.textChanged.connect(self.verificar_existencia_cedula)
        self.in_mail.editingFinished.connect(self.mostrar_mensaje_mail)
        self.in_number.textChanged.connect(self.mostrar_mensaje_telefono)
        self.users_dialog = None  # Definir users_dialog como un atributo de la clase

    def addPhoto(self):
        filenames, _ = QFileDialog.getOpenFileNames(self, "Seleccionar imágenes", "", "Archivos de imagen (*.png *.jpg *.bmp)")

        if len(filenames) >= 1:
            pixmap1 = QPixmap(filenames[0])
            self.foto.setPixmap(pixmap1)
        else:
            QMessageBox.information(self, "Imagenes", "Por favor, selecciona una imagen")

    def validar_correo_electronico(self, correo):
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(patron, correo) is not None

    def mostrar_mensaje_mail(self):
        correo = self.in_mail.text()
        if self.validar_correo_electronico(correo):
            self.btn_agg.setEnabled(True)
        else:
            QMessageBox.warning(self, "Correo invalido", "Por favor introduzca un correo valido")
            self.btn_agg.setEnabled(False)
            return

    def validar_numeros(self, cadena):
        patron = r'^[0-9]+$'
        return re.match(patron, cadena) is not None

    def mostrar_mensaje_telefono(self):
        numero = self.in_number.text()
        if self.validar_numeros(numero):
            self.btn_agg.setEnabled(True)
        else:
            QMessageBox.information(self, "Solo numeros", "Número inválido")
            self.btn_agg.setEnabled(False)
            return

    def clearInputs(self):
        self.in_cedula.clear()
        self.in_name.clear()
        self.in_apell.clear()
        self.in_age.clear()
        self.in_mail.clear()
        self.in_number.clear()
        self.in_dir.clear()
        self.btn_m.setChecked(False)
        self.btn_f.setChecked(False)
        self.in_espec.clear()
        self.foto.clear()

    def cifrar_contrasenia(self, contrasenia):
        cifrado = hashlib.sha256()
        cifrado.update(contrasenia.encode('utf-8'))
        return cifrado.hexdigest()

    def verificar_existencia_cedula(self):
        cedula = self.in_cedula.text()

        if not cedula:
            return

        conexion = sqlite3.connect('interfaces/database.db')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM Users WHERE Cedula = ?', (cedula,))
        existe_cedula = cursor.fetchone() is not None
        conexion.close()

        if existe_cedula:
            QMessageBox.warning(self, "Error", "Ya existe alguien con la misma cédula.")
            self.btn_agg.setEnabled(False)
            return
        else:
            self.btn_agg.setEnabled(True)

    def close(self):
        reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Desea Salir?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.Yes:
            QtWidgets.QApplication.quit()

    def usuario_existe(self, username):
        # Conectar a la base de datos
        conexion = sqlite3.connect('interfaces/database.db')
        # Crear un cursor
        cursor = conexion.cursor()
        # Consultar si el usuario ya existe
        cursor.execute('SELECT COUNT(*) FROM Users WHERE Username = ?', (username,))
        resultado = cursor.fetchone()[0]
        # Cerrar la conexión
        conexion.close()
        # Si resultado es mayor que 0, significa que el usuario ya existe
        return resultado > 0

    def registrarUsuario(self):
        cedula = self.in_cedula.text()
        nombre = self.in_name.text()
        apellido = self.in_apell.text()
        edad = self.in_age.text()
        mail = self.in_mail.text()
        valor_sexo = ""
        foto = self.foto.pixmap()
        if self.btn_m.isChecked():
            valor_sexo = "Masculino"
        elif self.btn_f.isChecked():
            valor_sexo = "Femenino"

        if not cedula or not nombre or not apellido or not edad or not valor_sexo or not mail:
            QMessageBox.critical(self, "Error", "Por favor, complete todos los campos básicos.")
            return

        self.datos_basicos = {
            'cedula': cedula,
            'nombre': nombre,
            'apellido': apellido,
            'edad': edad,
            'sexo': valor_sexo,
            'mail': mail,
        }

        # Mostrar diálogo para completar información adicional
        self.openUsersDialog()

    def guardarDatosUsuarios(self):
        username = self.users_dialog.in_user.text()
        password = self.users_dialog.in_password.text()
        passwordRepeat = self.users_dialog.in_conf.text()
        telefono = self.in_number.text()
        direccion = self.in_dir.text()
        especialidad = self.in_espec.text()
        foto = self.foto.pixmap()

        if not username or not password or not passwordRepeat or not telefono or not direccion or not especialidad:
            QMessageBox.critical(self, "Error", "Por favor, complete todos los campos de usuario.")
            return

        if len(password) < 8:
            QMessageBox.critical(self, "Error", "La contraseña debe tener mínimo 8 caracteres.")
            return

        if password != passwordRepeat:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden.")
            return

        if not foto:
            QMessageBox.warning(self, "Advertencia", "Debes importar una imagen antes de guardar.")
            return

        cedula = self.datos_basicos['cedula']
        nombre = self.datos_basicos['nombre']
        apellido = self.datos_basicos['apellido']
        edad = self.datos_basicos['edad']
        valor_sexo = self.datos_basicos['sexo']
        mail = self.datos_basicos['mail']

        # Validar si el nombre de usuario ya existe
        if self.usuario_existe(username):
            QMessageBox.warning(self, "Error", "El nombre de usuario ya existe. \nIngrese uno distinto")
            return

        # Cifrar la contraseña
        contrasenia_cifrada = self.cifrar_contrasenia(password)

        foto_image = foto.toImage()
        foto_bytes = QByteArray()
        buffer = QBuffer(foto_bytes)
        buffer.open(QIODevice.WriteOnly)
        foto_image.save(buffer, "PNG")
        foto_bytes = buffer.data()
        buffer.close()

        # Conectar a la base de datos
        conexion = sqlite3.connect('interfaces/database.db')
        # Crear un cursor
        cursor = conexion.cursor()
        # Insertar datos en la tabla Users
        cursor.execute(
            'INSERT INTO Users (Username, Password, Cedula, Nombres, Apellidos, Sexo, Edad, Direccion, Telefono, Mail, Especialidad, Imagen) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (username, contrasenia_cifrada, cedula, nombre, apellido, valor_sexo, edad, direccion, telefono, mail,
             especialidad, foto_bytes))
        # Confirmar la transacción
        conexion.commit()
        # Cerrar la conexión
        conexion.close()

        QMessageBox.information(self, "Éxito", "Registro exitoso")

        # Cerrar el diálogo de usuarios
        self.users_dialog.close()

    def openUsersDialog(self):
        # Crear una instancia del diálogo y asignarla como un atributo de la instancia de la clase
        self.users_dialog = QDialog(self)
        ui = Ui_Dialog()
        ui.setupUi(self.users_dialog)

        # Conectar la señal de aceptar en el diálogo de usuarios a una función
        ui.btn_agg.clicked.connect(self.guardarDatosUsuarios)

        # Acceder directamente a los atributos necesarios en el diálogo de usuarios
        self.users_dialog.in_user = self.users_dialog.findChild(QtWidgets.QLineEdit, 'in_user')
        self.users_dialog.in_password = self.users_dialog.findChild(QtWidgets.QLineEdit, 'in_password')
        self.users_dialog.in_conf = self.users_dialog.findChild(QtWidgets.QLineEdit, 'in_conf')

        self.users_dialog.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("si")

    SI = Registro()
    SI.showFullScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(SI)
    widget.setGeometry(SI.geometry())

    widget.show()
    sys.exit(app.exec_())