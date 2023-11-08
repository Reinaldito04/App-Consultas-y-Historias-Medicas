import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import sqlite3

class Ui_pacientes_view(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_pacientes_view, self).__init__()
        loadUi("./interfaces/paciente_view.ui", self)
        self.actionSalir.triggered.connect(self.salir)
        self.bt_act.clicked.connect(self.act_T)
        self.bt_buscar.clicked.connect(self.buscar)

        self.filtro = self.findChild(QtWidgets.QComboBox, "filtro")
        self.filtro.addItem("Seleccione una opción para filtrar")
        self.filtro.addItems(["Cedula", "Nombre", "Edad", "Genero", "Fecha"])

    def act_T(self):
        self.cargarPacientes()

    def cargarPacientes(self):
        model = QtGui.QStandardItemModel()
        self.tabla_p.setModel(model)
        headers = ["Cedula", "Nombre", "Apellido", "Edad", "Dirección", "Sexo", "Fecha"]
        model.setColumnCount(len(headers))
        model.setHorizontalHeaderLabels(headers)

        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()

            # Obtén el ID del usuario actual
            id_User = self.id_User  # Asegúrate de que esta variable esté definida y tenga el valor correcto

            # Ejecuta una consulta para obtener los datos de los pacientes y ordenar por Fecha_Cita descendente
            cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Direccion, Sexo, Fecha_Cita FROM Pacientes WHERE ID_user = ? ORDER BY Fecha_Cita ASC", (id_User,))
            pacientes = cursor.fetchall()

            for row, paciente in enumerate(pacientes):
                for column, value in enumerate(paciente):
                    item = QtGui.QStandardItem(str(value))
                    model.setItem(row, column, item)

            conexion.close()
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, "Error", "Error al consultar la base de datos: " + str(e))

    def buscar(self):
        if self.filtro.currentIndex() == 0:
            QtWidgets.QMessageBox.warning(self, "Error", "Debe seleccionar un filtro para buscar")
        else:
            filtro = self.filtro.currentText()
            valor = self.in_buscar.text()
            self.buscarPacientes(filtro, valor)

    def buscarPacientes(self, filtro, valor):
        print("si")

    def salir(self):
        reply = QtWidgets.QMessageBox.question(
            self, 'Confirmación', '¿Desea Salir?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes
        )
        if reply == QtWidgets.QMessageBox.Yes:
            QtWidgets.QApplication.quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("si")  # Establecer el nombre de la aplicación

    Vista_P = Ui_pacientes_view()
    Vista_P.showFullScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(Vista_P)
    widget.setGeometry(Vista_P.geometry())
    widget.show()
    sys.exit(app.exec_())
