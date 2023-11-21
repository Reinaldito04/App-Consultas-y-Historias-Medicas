import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate, QTime
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QApplication
import sqlite3

class Ui_CitasMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_CitasMenu, self).__init__()
        loadUi("interfaces/citas.ui", self)
        self.actionSalir.triggered.connect(self.salir)
        self.btn_buscar.clicked.connect(self.searchdata)
        self.btn_agg.clicked.connect(self.aggCite)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_edit.clicked.connect(self.editarCita)
        self.setWindowTitle("Menu de Citas")
        self.showMaximized()

    def eliminarCita(self):
        try:
            cedula = self.in_busqueda.text()

            if len(cedula) == 0:
                QMessageBox.critical(self, "Error", "Ingrese una cédula")
            else:
                citaNull = None
                horaNull = None
                conexion = sqlite3.connect('/Users/Estudiante/Downloads/database.db')
                cursor = conexion.cursor()
                cursor.execute("UPDATE Pacientes SET Fecha_Cita = ?, Hora_Cita = ? WHERE Cedula = ?",
                               (citaNull, horaNull, cedula))
                conexion.commit()
                conexion.close()

                QMessageBox.information(self, "Realizado", "La cita ha sido eliminada correctamente")

                self.clear()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", "Error al eliminar la cita de la base de datos: " + str(e))

    def clear(self):
        self.in_busqueda.clear()
        self.txt_name.clear()
        self.txt_apell.clear()
        self.tableWidget.setRowCount(0)

    def editarCita(self):
        cedula = self.in_busqueda.text()

        fecha = self.fecha.selectedDate()
        fechaToString = fecha.toString('yyyy-MM-dd')
        statusCita = 'Activa' if self.bt_act.isChecked() else 'Cancelada' if self.bt_cancel.isChecked() else None
        hora = self.hora.time()
        horaToString = hora.toString('hh:mmm:ss')

        try:
            if not cedula:
                QMessageBox.warning(self, "Introduzca una cedula", "Debes introducir una cedula antes de editar")
                return

            # Verificar si la nueva fecha y hora ya están asignadas a otra cita
            conexion = sqlite3.connect('/Users/Estudiante/Downloads/database.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM Cita WHERE Fecha_Cita = ? AND Hora_Cita = ? AND Cedula != ?",
                           (fechaToString, horaToString, cedula))
            existe_otra_cita = cursor.fetchone()[0] > 0

            if existe_otra_cita:
                QMessageBox.warning(self, "Advertencia", "La fecha y hora seleccionadas ya están asignadas a otra cita.")
            else:
                reply = QMessageBox.question(
                    self,
                    'Confirmación',
                    '¿Desea cambiar la fecha y hora de la cita?',
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.Yes
                )

                if reply == QMessageBox.Yes:
                    cursor.execute("UPDATE Cita SET Fecha_Cita = ?, Hora_Cita = ?, Estatus_Cita = ? WHERE Cedula = ?",
                                   (fechaToString, horaToString, statusCita, cedula))
                    conexion.commit()
                    QMessageBox.information(self, "Información", "Cita actualizada con éxito.")

            conexion.close()

        except sqlite3.Error as error:
            QMessageBox.critical(self, "Error", f"Error al actualizar la cita: {str(error)}")


    def aggCite(self):
        cedula = self.in_busqueda.text()

        fecha = self.fecha.selectedDate()
        fechaToString = fecha.toString('yyyy-MM-dd')
        statusCita = 'Activa' if self.bt_act.isChecked() else 'Cancelada' if self.bt_cancel.isChecked() else None
        hora = self.hora.time()
        horaToString = hora.toString('hh:mm:ss')

        try:
                if not cedula:
                        QMessageBox.warning(self, "Introduzca una cedula", "Debes introducir una cedula antes de guardar")
                        return

                # Verificar si el paciente ya tiene una cita programada para la fecha y hora seleccionadas
                conexion = sqlite3.connect('/Users/Estudiante/Downloads/database.db')
                cursor = conexion.cursor()
                cursor.execute("SELECT COUNT(*) FROM Cita WHERE Cedula = ? AND Fecha_Cita = ? AND Hora_Cita = ?",
                        (cedula, fechaToString, horaToString))
                existe_cita_paciente = cursor.fetchone()[0] > 0

                if existe_cita_paciente:
                        QMessageBox.warning(self, "Advertencia", "El paciente ya tiene una cita programada para esta fecha y hora.")
                else:
                # Verificar si el paciente ya tiene una cita programada para otra fecha y hora
                        cursor.execute("SELECT COUNT(*) FROM Cita WHERE Cedula = ? AND (Fecha_Cita != ? OR Hora_Cita != ?)",
                                        (cedula, fechaToString, horaToString))
                        existe_otra_cita_paciente = cursor.fetchone()[0] > 0

                        if existe_otra_cita_paciente:
                                QMessageBox.warning(self, "Advertencia", "El paciente ya tiene una cita programada para otra fecha y hora.")
                        else:
                                # Si no existe una cita, inserta una nueva cita
                                cursor.execute("INSERT INTO Cita (Cedula, Fecha_Cita, Hora_Cita, Estatus_Cita) VALUES (?, ?, ?, ?)",
                                        (cedula, fechaToString, horaToString, statusCita))
                                QMessageBox.information(self, "Información", "Cita agregada con éxito.")

                        conexion.commit()
                        conexion.close()

        except sqlite3.Error as error:
                QMessageBox.critical(self, "Error", f"Error al agregar la cita: {str(error)}")

                
    def searchdata(self):
        cedula = self.in_busqueda.text()

        if len(cedula) <= 0:
            QMessageBox.warning(self, "Error", "Ingrese una cedula")
            return  # Salir de la función si no hay cédula

        try:
            conexion = sqlite3.connect('/Users/Estudiante/Downloads/database.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT C.Nombre, C.Apellido, Ci.Fecha_Cita, Ci.Hora_Cita, Ci.Estatus_Cita "
                           "FROM Cita Ci "
                           "JOIN Pacientes C ON Ci.Cedula = C.Cedula "
                           "WHERE C.Cedula = ?", (cedula,))
            tabla_cita = cursor.fetchall()

            resultados_filtrados = [resultado for resultado in tabla_cita if None not in resultado]

            if resultados_filtrados:
                self.tableWidget.clearContents()
                self.tableWidget.setRowCount(len(resultados_filtrados))
                self.tableWidget.setColumnCount(len(resultados_filtrados[0]))
                for row, cita in enumerate(resultados_filtrados):
                    for column, value in enumerate(cita):
                        item = QTableWidgetItem(str(value))
                        self.tableWidget.setItem(row, column, item)

                primer_resultado = resultados_filtrados[0]
                cedula_paciente,nombre_paciente, apellido_paciente, fechaCita, horaCita, status_cita = primer_resultado
                cedula_paciente=cedula
                self.txt_name.setText(nombre_paciente)
                self.txt_apell.setText(apellido_paciente)
                fecha_cita = fechaCita
                self.fecha.setSelectedDate(QDate.fromString(fecha_cita, 'yyyy-MM-dd'))
                hora_cita = QTime.fromString(horaCita, 'hh:mm:ss')
                status_cita = primer_resultado[4]
                if status_cita == 'Activa':
                    self.bt_act.setChecked(True)
                if status_cita == 'Cancelada':
                    self.bt_cancel.setChecked(True)

                self.hora.setTime(hora_cita)
            else:
                QMessageBox.warning(self, "Sin resultados", "El paciente no tiene citas actualmente")
                cursor.execute("SELECT Nombre, Apellido FROM Pacientes WHERE Cedula = ?", (cedula,))
                datos_paciente = cursor.fetchone()

                if datos_paciente:
                    nombre_paciente, apellido_paciente = datos_paciente
                    self.txt_name.setText(nombre_paciente)
                    self.txt_apell.setText(apellido_paciente)
                else:
                    QMessageBox.warning(self, "Sin resultados", "No se encontró al paciente")

        except sqlite3.Error as error:
            QMessageBox.critical(self, "Error", f"Error al buscar paciente: {str(error)}")
        finally:
            conexion.close()

    def salir(self):
        reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Desea Salir?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.Yes:
            QApplication.quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("si")
    citas = Ui_CitasMenu()
    citas.showFullScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(citas)
    widget.setGeometry(citas.geometry())

    widget.show()
    sys.exit(app.exec_())
