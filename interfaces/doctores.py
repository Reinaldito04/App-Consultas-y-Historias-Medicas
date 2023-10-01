from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import sqlite3

class Ui_doctores(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_doctores, self).__init__()
        loadUi("interfaces\dogtores.ui", self)
        self.btn_agg.clicked.connect(self.Aggdoctor)
        self.btn_clear.clicked.connect(self.clearInputs)
        self.actionSalir.triggered.connect(self.salir)
       
    def salir(self):
        QtWidgets.qApp.quit()

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
        self.in_busqueda.clear()
        self.in_user.clear()
        self.in_password.clear()
        self.in_valid_password.clear()
    def Aggdoctor(self):
        cedula = self.in_cedula.text()
        nombre = self.in_name.text()
        apellido = self.in_apell.text()
        edad = self.in_age.text()
        mail = self.in_mail.text()
        valor_sexo = ""
        
        if self.btn_m.isChecked():
            valor_sexo = "Masculino"
        elif self.btn_f.isChecked():
            valor_sexo = "Femenino"

        telefono = self.in_number.text()
        direccion = self.in_dir.text()
        especialidad = self.in_espec.text()

        if not cedula or not nombre or not apellido or not edad or not valor_sexo or not mail or not telefono or not direccion or not especialidad:
            QMessageBox.critical(self, "Error", "Por favor, complete todos los campos.")
            return

        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()

            # Verificar si ya existe un doctor con la misma cédula
            cursor.execute("SELECT COUNT(*) FROM Users WHERE Cedula = ?", (cedula,))
            existe_doctor = cursor.fetchone()[0]

            if existe_doctor > 0:
                QMessageBox.critical(self, "Error", "Ya existe un Doctor con la misma cédula.")
                # Limpia los campos después de denegar el ingreso
                self.clearInputs()
                return

            # Si no existe un doctor con la misma cédula, ejecutar la consulta de inserción
            cursor.execute("INSERT INTO Users (Cedula, Nombres, Apellidos, Edad, Sexo, Direccion, Telefono, Mail, Especialidad) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (cedula, nombre, apellido, edad, valor_sexo, direccion, telefono, mail, especialidad))

            # Confirmar los cambios en la base de datos
            conexion.commit()
            QMessageBox.information(self, "Éxito", "Doctor registrado correctamente.")

            # Limpia los campos después de agregar el doctor
            self.clearInputs()

            # Cierra la conexión con la base de datos
            conexion.close()

        except sqlite3.Error as error:
            QMessageBox.critical(self, "Error", f"Error al registrar doctor: {str(error)}")

   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registrodoctores = Ui_doctores()
    registrodoctores.show()
    sys.exit(app.exec_())
