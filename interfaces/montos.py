import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import sqlite3
import re
class Ui_montos(QMainWindow):
    def __init__(self):
        super(Ui_montos, self).__init__()
        loadUi("./interfaces/montos.ui", self)
        self.setWindowTitle("Montos")

        self.tratamientos = {
            "Triaje": ["Consulta e Historia Clínica sin informe", "Consulta e Historia Clínica con informe"],
            "Periodoncia": ["Tartectomía y pulido simple (1 sesión)", "Tartectomía y pulido simple (2-3 sesiones)","Aplicación tópica de fluór","Cirguia periodontal (por cuadrante)"],
            "Blanqueamiento": ["Blanqueamiento intrapulpar", "Blanquemaineto maxilar superior e inferior (2 sesiones de 20 min c/u)"],
            "Operatoria": ["Obturaciones provisionales","Obturaciones con Amalgama","Obturaciones con vidrio ionomerico pequeña","Obturaciones con vidrio ionomerico grande","Obturaciones con resina fotocurada"],
            "Endodoncia": ["Pulpotomías formocreasoladas","Emergencias Endodontica","Tratamiento endodontico monoradicular","Tratamiento endodontico biradicular","Tratamiento endodontico multiradicular","Desobturación conductos"],
            "Radiografias Periaciales": ["Adultos e infantes"],
            "Cirugias": ["Exodoncia simple","Exodoncia quirurgica","Exodoncia de dientes temporales","Exodoncia de corales erupcionadas/incluidas"],
            "Protesis": ["Coronas provisionales por unidad","Muñon artificial monoradicular","Muñon artificial multiradicular","Incrustacion resina/metálica","Unidad de corona meta-porcelana","Cementado de protesis fija"],
            "Protesis removibles metalicas y/o acrilicas": ["1 a 3 unidades","4 a 6 unidades","7 a 12 unidades","Unidadad adicional","Ganchos contorneados retentativas acrilicas c/u","Reparaciones protesis acrilicas y/oo agregar un diente a la protesis"],
            "Protesis totales": ["Dentadura superior o inferior (incluye controles post-inatalción) c/u"],
            "Implantes dentales": ["Honorarios cirujano por implante","Implante y aditamientos","Injertos óseos (1cc)","PRF (incluye bionalista y extraccion de sangre + centrifugado)","Corona metal porcelana sobre implante","DPR acrilica"],
        }

        self.btn_agg.clicked.connect(self.aggMontos)
        self.btn_clear.clicked.connect(self.clear)
        self.actionSalir.triggered.connect(self.salir)

        self.t_0 = self.findChild(QtWidgets.QComboBox, "t_0")
        self.t_0.addItem("Seleccione el tipo de honorario")
        self.t_0.addItems(list(self.tratamientos.keys()))

        self.t_0.currentTextChanged.connect(self.loadTratamientos)

        self.loadTratamientos()

    def loadTratamientos(self):
        self.clear()
        seleccion_t_0 = self.t_0.currentText()
        if seleccion_t_0 == "Seleccione el tipo de honorario":
            return

        tratamientos_honorario = self.tratamientos.get(seleccion_t_0, [])

        for i, tratamiento in enumerate(tratamientos_honorario, start=1):
            getattr(self, f't_{i}').setText(tratamiento)

    def aggMontos(self):
        tipo_tratamiento = self.t_0.currentText()

        tratamientos_montos = []
        num_montos_introducidos = 0
        
        for i in range(1, 7):
            tratamiento = getattr(self, f't_{i}').text()
            monto = getattr(self, f'monto_{i}').text()

            # Verifica si el tratamiento y el monto no están vacíos
            if tratamiento and monto:
                if not re.match(r'^-?\d*\.?\d+$', monto):
                    QMessageBox.warning(self, "Error", "Por favor, ingrese solo números en el campo de monto.")
                    self.clear()
                    return  

                
                tratamientos_montos.append((tratamiento, monto))
                num_montos_introducidos += 1  # Incrementa el contador
        if num_montos_introducidos == 0:
            QtWidgets.QMessageBox.warning(None, 'Error', 'No se han introducido montos')
            return
        
        
        montos=QMessageBox.question(self, "Cantidad de Montos",
                                    f"Se han introducido {num_montos_introducidos} montos.\n¿Deseas seguir con la ejecución?",
                                    QMessageBox.Yes | QMessageBox.No
                                     )

        if montos == QMessageBox.Yes:
            if len(tipo_tratamiento) <= 0:
                QMessageBox.warning(self, "Advertencia", "Debes ingresar el tipo de tratamiento")
                return

            try:
                # Conecta a la base de datos y almacena los datos
                conexion = sqlite3.connect('interfaces/database.db')
                cursor = conexion.cursor()

                # Verifica si el tratamiento ya existe en la base de datos
                for tratamiento, monto in tratamientos_montos:
                    cursor.execute("SELECT monto FROM Trata WHERE tipo_tratamiento = ? AND tratamiento = ?", (tipo_tratamiento, tratamiento))
                    existing_record = cursor.fetchone()

                    if existing_record:
                        # Si existe el tratamiento, preguntar al usuario si desea actualizar el monto
                        update = QMessageBox.question(self, "Tratamiento Existente",
                                                    f"El tratamiento '{tratamiento}' ya existe con un monto de '{existing_record[0]}'. ¿Desea actualizar el monto?",
                                                    QMessageBox.Yes | QMessageBox.No)

                        if update == QMessageBox.Yes:
                            cursor.execute("UPDATE Trata SET monto = ? WHERE tipo_tratamiento = ? AND tratamiento = ?",
                                        (monto, tipo_tratamiento, tratamiento))
                            QMessageBox.information(self, "Éxito", f"¡Monto actualizado para el tratamiento '{tratamiento}'!")
                    else:
                        # Si no existe, insertar el nuevo tratamiento y monto
                        cursor.execute("INSERT INTO Trata (tipo_tratamiento, tratamiento, monto) VALUES (?, ?, ?)",
                                    (tipo_tratamiento, tratamiento, monto))
                        QMessageBox.information(self, "Éxito", "Datos de tratamientos añadidos correctamente")

                for i in range(1, 7):
                    getattr(self, f't_{i}').clear()
                    getattr(self, f"monto_{i}").clear()

                conexion.commit()
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", "Error al insertar o actualizar datos en la base de datos: " + str(e))
            finally:
                conexion.close()
        else:
            self.clear()

    def clear(self):
        for i in range(1, 7):
            getattr(self, f't_{i}').clear()
            getattr(self, f"monto_{i}").clear()

    def salir(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("si")  # Establecer el nombre de la aplicación

    Montos = Ui_montos()
    Montos.showFullScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(Montos)
    widget.setGeometry(Montos.geometry())

    widget.show()
    sys.exit(app.exec_())