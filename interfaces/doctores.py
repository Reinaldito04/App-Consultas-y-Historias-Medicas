from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import sqlite3

class Ui_doctores(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_doctores, self).__init__()
        loadUi("interfaces\dogtores.ui", self)

        self.btn_buscar.clicked.connect(self.Searchdata)
        self.btn_agg.clicked.connect(self.Aggdoctor)
        self.btn_clear.clicked.connect(self.clearInputs)
        self.btn_edit.clicked.connect(self.UpdateData)
        self.actionSalir.triggered.connect(self.salir)
        self.btn_delete.clicked.connect(self.DeletaData)

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
            cursor.execute("SELECT COUNT(*) FROM Doctores WHERE Cedula = ?", (cedula,))
            existe_doctor = cursor.fetchone()[0]

            if existe_doctor > 0:
                QMessageBox.critical(self, "Error", "Ya existe un Doctor con la misma cédula.")
                # Limpia los campos después de denegar el ingreso
                self.clearInputs()
                return

            # Si no existe un doctor con la misma cédula, ejecutar la consulta de inserción
            cursor.execute("INSERT INTO Doctores (Cedula, Nombre, Apellido, Edad, Sexo, Direccion, Telefono, Mail, Especialidad) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
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

    def Searchdata(self):
        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
            busqueda = self.in_busqueda.text()
            cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Direccion, Sexo, Telefono, Mail, Especialidad FROM Doctores WHERE Cedula = ?", (busqueda,))
            resultado = cursor.fetchone()

            if resultado:
                Cedula, Nombre, Apellido, Edad, Direccion, Sexo, Telefono, Mail, Especialidad = resultado

                self.in_cedula.setText(Cedula)
                self.in_name.setText(Nombre)
                self.in_apell.setText(Apellido)
                self.in_age.setText(str(Edad))
                self.in_mail.setText(Mail)
                self.in_dir.setText(Direccion)
                self.in_number.setText(Telefono)
                self.in_espec.setText(Especialidad)

                # Manejar los botones de radio según el valor de Sexo
                if Sexo == "Masculino":
                    self.btn_m.setChecked(True)
                elif Sexo == "Femenino":
                    self.btn_f.setChecked(True)

            else:
                # Limpiar la tabla existente si no se encuentra ningún registro
                self.tabla_doctores.clearContents()
                QMessageBox.warning(self, "Advertencia", "No se ha encontrado ningún registro")

            conexion.close()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", "Error al consultar la base de datos: " + str(e))

    def UpdateData(self):
        try:
            cedula = self.in_cedula.text()
            nombre = self.in_name.text()
            apellido = self.in_apell.text()
            edad = self.in_age.text()
            direccion = self.in_dir.text()
            telefono = self.in_number.text()
            mail = self.in_mail.text()
            especialidad = self.in_espec.text()
            valor_sexo = "Masculino" if self.btn_m.isChecked() else "Femenino"

            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()

            # Actualizar los registros en la base de datos
            cursor.execute("UPDATE Doctores SET Nombre=?, Apellido=?, Edad=?, Direccion=?, Sexo=?, Telefono=?, Mail=?, Especialidad=? WHERE Cedula=?", (nombre, apellido, edad, direccion, valor_sexo, telefono, mail, especialidad, cedula))
            conexion.commit()

            QMessageBox.information(self, "Información", "Los datos se actualizaron correctamente")

            conexion.close()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", "Error al actualizar los datos en la base de datos: " + str(e))

    def DeletaData(self):
        try:
            cedula = self.in_cedula.text()

            if len(cedula) == 0:
                QMessageBox.critical(self, "Error", "Ingrese una cédula")
            else:
                conexion = sqlite3.connect('interfaces/database.db')
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM Doctores WHERE Cedula = ?", (cedula,))
                conexion.commit()
                conexion.close()

                # Eliminación exitosa, muestra un mensaje y realiza otras acciones si es necesario
                QMessageBox.information(self, "Realizado", "Los datos han sido eliminados correctamente")
                self.clearInputs()
                self.in_busqueda.clear()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", "Error al eliminar los datos de la base de datos: " + str(e))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registrodoctores = Ui_doctores()
    registrodoctores.show()
    sys.exit(app.exec_())
