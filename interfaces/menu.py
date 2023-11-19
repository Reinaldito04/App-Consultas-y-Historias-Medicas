import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLabel, QTableWidgetItem
from PyQt5.uic import loadUi
import sqlite3

class QMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        loadUi("./interfaces/menu.ui", self)
        self.bt_act.clicked.connect(self.act_T)
        self.bt_buscar.clicked.connect(self.buscar)
        self.cargarCitas()
        self.filtro = self.findChild(QtWidgets.QComboBox, "filtro")
        self.filtro.addItem("Seleccione una opción para filtrar")
        self.filtro.addItems(["Dentista", "Cedula", "Nombre", "Fecha_Cita", "Hora_Cita", "Status_Cita"])
        self.in_buscar.textChanged.connect(self.buscar)

    def act_T(self):
        self.cargarCitas()

    def cargarCitas(self, filtro=None, valor=None):
        self.tabla_cita.setRowCount(0)  # Limpiar la tabla actual
        headers = ["Cedula", "Nombre", "Apellido", "Fecha de la  cita", "Hora de la cita", "Estatus de la cita"]

        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()

            if filtro and valor:
                cursor.execute("SELECT Cedula, Nombre, Apellido, Fecha_Cita, Hora_Cita, Status_Cita FROM Pacientes WHERE {} LIKE ? ORDER BY Fecha_Cita ASC".format(filtro), ('%' + valor + '%',))
            else:
                cursor.execute("SELECT Cedula, Nombre, Apellido, Fecha_Cita, Hora_Cita, Status_Cita FROM Pacientes ORDER BY Fecha_Cita ASC")

            citas = cursor.fetchall()

            self.tabla_cita.setColumnCount(len(headers))
            self.tabla_cita.setHorizontalHeaderLabels(headers)

            for row, cita in enumerate(citas):
                self.tabla_cita.insertRow(row)
                for column, value in enumerate(cita):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.tabla_cita.setItem(row, column, item)

            conexion.close()
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, "Error", "Error al consultar la base de datos: " + str(e))

    def buscar(self):
        filtro = self.filtro.currentText()
        valor = self.in_buscar.text()
        if filtro == "Seleccione una opción para filtrar":
            QtWidgets.QMessageBox.warning(self, "Error", "Debe seleccionar un filtro para buscar")
        elif len(valor) == 0:
            self.act_T()
        elif not valor:
            QtWidgets.QMessageBox.warning(self, "Por favor", "Ingrese alguna especificación de la cita para realizar la búsqueda")
        elif self.tabla_cita.rowCount() == 0:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No se ha encontrado ninguna cita")
        else:
            self.cargarCitas(filtro, valor)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("si")

    Vista_C = QMainWindow()
    Vista_C.showFullScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(Vista_C)
    widget.setGeometry(Vista_C.geometry())
    widget.show()
    sys.exit(app.exec_())
