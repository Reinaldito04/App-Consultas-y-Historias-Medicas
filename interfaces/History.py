from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
import sqlite3
import datetime

class historiaMenu(QMainWindow):
    
    def __init__(self):
        super(historiaMenu, self).__init__()
        loadUi("interfaces/History.ui", self)
        self.btn_buscar.clicked.connect(self.Searchdata)
        self.actionSalir.triggered.connect(self.salir)

        self.t0 = self.findChild(QtWidgets.QComboBox, "t0")
        self.t0.addItem("Seleccione el tipo de honorario")
        self.t0.addItems(["Triaje", "Periodoncia", "Blanqueamiento", "Operatoria", "Endodoncia", "Radiografias Periaciales", "Cirugias", "Protesis", "Protesis removibles metalicas y/o acrilicas", "Protesis totales", "Implantes dentales"])
        self.t0.currentIndexChanged.connect(self.actualizar_cb_tratamiento)

        self.t1 = self.findChild(QtWidgets.QComboBox, "t1")
        self.t2 = self.findChild(QtWidgets.QComboBox, "t2")
        self.t3 = self.findChild(QtWidgets.QComboBox, "t3")
        
        # Define el diccionario de tratamientos
        self.tratamientos = {
            "Triaje": ["Consulta e Hisotia Clinica sin informe", "Consulta e Hisotia Clinica con informe"],
            "Periodoncia": ["Tartectomia y pulido simple (1 sesión)", "Tartectomia y pulido simple (2-3 sesiones)","Aplicación tópica de fluór","Cirguia periodontal (por cuadrante)"],
            "Blanqueamiento": ["Blanqueamiento intrapulpar", "Blanquemaineto maxilar superior e inferioir (2 sesiones de 20 min c/u)"],
            "Operatoria": ["Obturaciones provisionales","Obturaciones con Amalgama","Obturaciones con vidrio ionomerico pequeña","Obturaciones con vidrio ionomerico grande","Obturaciones con resina fotocurada"],
            "Endodoncia": ["Pulpotomías formocreasoladas","Emergencias Endodontica","Tratamiento endodontico monoradicular","Tratamiento endodontico biradicular","Tratamiento endodontico multiradicular","Desobturación conductos"],
            "Radiografias Periaciales": ["Adultos e infantes"],
            "Cirugias": ["Exodoncia simple","Exodoncia quirurgica","Exodoncia de dientes temporales","Exodoncia de corales erupcionadas/incluidas"],
            "Protesis": ["Coronas provisionales por unidad","Muñon artificial monoradicular","Muñon artificial multiradicular","Incrustacion resina/metálica","Unidad de corona meta-porcelana","Cementado de protesis fija"],
            "Protesis removibles metalicas y/o acrilicas": ["1 a 3 unidades","4 a 6 unidades","7 a 12 unidades","Unidadad adicional","Ganchos contorneados retentativas acrilicas c/u","Reparaciones protesis acrilicas y/oo agregar un diente a la protesis"],
            "Protesis totales": ["Dentadura superior o inferior (incluye controles post-inatalción) c/u"],
            "Implantes dentales": ["Honorarios cirujano por implante","Implante y aditamientos","Injertos óseos (1cc)","PRF (incluye bionalista y extraccion de sangre + centrifugado)","Corona metal porcelana sobre implante","DPR acrilica"],
        }
        
    def salir(self):
        QApplication.quit()
        
    def Searchdata(self):
        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
            idUser = self.id_user
            busqueda = self.in_busqueda.text()
            cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Direccion, Sexo, Telefono, Mail, Context, Hipertension, Diabates, Coagualcion, Otros, Alergias, diabate_Data, hipertension_Data, Coagualcion_Data FROM Pacientes WHERE Cedula = ? AND ID_user = ?", (busqueda, idUser))
            resultado = cursor.fetchone()
            
            if resultado:
                # Carga los datos del paciente en los campos correspondientes
                # ...

                # Actualiza las ComboBoxes de tratamiento
                self.actualizar_cb_tratamiento()
            else:
                # No se encontró ningún registro, limpiar la tabla existente
                self.tabla_pacientes.clearContents()
                QMessageBox.warning(self, "Advertencia", "No se ha encontrado ningún registro")

            conexion.close()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", "Error al consultar la base de datos: " + str(e))
            
    def actualizar_cb_tratamiento(self):
        # Obtiene la selección en t0
        seleccion_t0 = self.t0.currentText()

        # Limpia las ComboBox t1, t2, t3
        self.t1.clear()
        self.t2.clear()
        self.t3.clear()

        # Obtiene las opciones de tratamiento según la selección en t0
        opciones_tratamiento = self.tratamientos.get(seleccion_t0, [])

        # Agrega las opciones a las ComboBox correspondientes
        self.t1.addItems(opciones_tratamiento)
        self.t2.addItems(opciones_tratamiento)
        self.t3.addItems(opciones_tratamiento)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    historias = historiaMenu()
    historias.show()
    sys.exit(app.exec_())
