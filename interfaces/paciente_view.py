import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QLabel,QTableWidgetItem
from PyQt5.uic import loadUi
import sqlite3

class Ui_pacientes_view(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_pacientes_view, self).__init__()
        loadUi("./interfaces/paciente_view.ui", self)
        self.actionSalir.triggered.connect(self.salir)
        self.bt_act.clicked.connect(self.act_T)
        self.bt_buscar.clicked.connect(self.buscar)
        self.cargarPacientes()
        self.filtro = self.findChild(QtWidgets.QComboBox, "filtro")
        self.filtro.addItem("Seleccione una opción para filtrar")
        self.filtro.addItems(["Dentista","Cedula", "Nombre", "Edad", "Sexo","Direccion" , "Fecha_Diagnotico"])
        
    def act_T(self):
        self.cargarPacientes()

    def cargarPacientes(self, filtro=None, valor=None):
        self.tabla_p.setRowCount(0)  # Limpiar la tabla actual
        headers = ["Cedula", "Nombre", "Apellido", "Edad", "Dirección", "Sexo", "Fecha_Diagnotico"]

        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()

            if filtro and valor:
                cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Direccion, Sexo, Fecha_Diagnotico FROM Pacientes WHERE {} LIKE ? ORDER BY Fecha_Diagnotico ASC".format(filtro), ('%' + valor + '%',))
            else:
                cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Direccion, Sexo, Fecha_Diagnotico FROM Pacientes ORDER BY Fecha_Diagnotico ASC")

            pacientes = cursor.fetchall()

            self.tabla_p.setColumnCount(len(headers))
            self.tabla_p.setHorizontalHeaderLabels(headers)

            for row, paciente in enumerate(pacientes):
                self.tabla_p.insertRow(row)
                for column, value in enumerate(paciente):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.tabla_p.setItem(row, column, item)

            conexion.close()
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, "Error", "Error al consultar la base de datos: " + str(e))
        
    def buscar(self):
        filtro = self.filtro.currentText()
        valor = self.in_buscar.text()
        if filtro == "Seleccione una opción para filtrar":
            QtWidgets.QMessageBox.warning(self, "Error", "Debe seleccionar un filtro para buscar")
        elif not valor:
            QtWidgets.QMessageBox.warning(self, "Por favor", "Ingrese alguna especificación del paciente para realizar la búsqueda")
        elif self.tabla_p.rowCount() == 0:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No se ha encontrado ningún registro")  
        else:
            self.cargarPacientes(filtro, valor)
        
    def salir(self):
        reply = QtWidgets.QMessageBox.question(
            self, 'Confirmación', '¿Desea Salir?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes
        )
        if reply == QtWidgets.QMessageBox.Yes:
            QtWidgets.QApplication.quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("si") 

    Vista_P = Ui_pacientes_view()
    Vista_P.showFullScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(Vista_P)
    widget.setGeometry(Vista_P.geometry())
    widget.show()
    sys.exit(app.exec_())
