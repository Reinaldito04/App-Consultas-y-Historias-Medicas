from PyQt5 import QtWidgets, QtGui, QtCore,QMessageBox, QTableWidgetItem
import sqlite3

class Ui_registrocitas(object):

    def setupUi(self, registrocitas):
        # Conecta los botones a las funciones correspondientes
        self.btn_citas.clicked.connect(self.mostrarCitas)
        self.btn_agg_cita.clicked.connect(self.mostrarFormularioAgendarCita)
        self.btn_borrar.clicked.connect(self.mostrarFormularioEliminarCita)
        self.btn_back.clicked.connect(self.volverAlMenu)
        self.btn_buscar.clicked.connect(self.buscarCitas)
        self.btn_buscar_2.clicked.connect(self.buscarPacienteParaCita)
        self.btn_edit.clicked.connect(self.editarCita)
        self.btn_agg.clicked.connect(self.agendarCita)
        self.btn_buscar_3.clicked.connect(self.buscarCitaParaEliminar)
        self.btn_delete.clicked.connect(self.eliminarCita)

    # Función para mostrar citas disponibles
    def mostrarCitas(self):
        self.stackedWidget.setCurrentWidget(self.tabla_citas)
        
    # Función para mostrar el formulario de agendar cita
    def mostrarFormularioAgendarCita(self):
        self.stackedWidget.setCurrentWidget(self.agg_cita)

    # Función para mostrar el formulario de eliminar cita
    def mostrarFormularioEliminarCita(self):
        self.stackedWidget.setCurrentWidget(self.delete_cita)

    # Función para volver al menú principal
    def back_menu(self):
        print("Volviendo al menú principal")
        menu_principal = "ya tu sabe que va aqui" (self.id_user)
        conexion =sqlite3.connect('interfaces/database.db')
        cursor= conexion.cursor()
        cursor.execute("SELECT Username FROM Users WHERE ID = ?", (self.id_user,))
        
        resultado= cursor.fetchone()
        if resultado :
            nombre_usuario= resultado[0]
            menu_principal.lb_nombre.setText(nombre_usuario)
            menu_principal.show()
            self.hide()
        pass

    # Función para buscar citas
    def buscarCitas(self):
        # Agrega aquí el código para buscar citas
        pass

    # Función para buscar paciente para asignar cita
    def buscarPacienteParaCita(self):
        # Agrega aquí el código para buscar un paciente para asignarle una cita
        pass

    # Función para editar una cita
    def editarCita(self):
        # Agrega aquí el código para editar una cita
        pass

    # Función para agendar una cita
    def agendarCita(self):
        # Agrega aquí el código para agendar una cita
        pass

    # Función para buscar una cita para eliminar
    def buscarCitaParaEliminar(self):
        # Agrega aquí el código para buscar una cita para eliminar
        pass

    # Función para eliminar una cita
    def eliminarCita(self):
        # Agrega aquí el código para eliminar una cita
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registrocitas = QtWidgets.QMainWindow()
    ui = Ui_registrocitas()
    ui.setupUi(registrocitas)
    registrocitas.show()
    sys.exit(app.exec_())
