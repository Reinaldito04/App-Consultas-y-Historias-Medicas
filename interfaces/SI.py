import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import sqlite3

class Ui_SI(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_SI, self).__init__()
        loadUi("./interfaces/SI.ui", self)
        self.setWindowTitle("SI")

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

        self.c_0 = self.findChild(QtWidgets.QComboBox, "c_0")
        self.c_1 = self.findChild(QtWidgets.QComboBox, "c_1")
        self.c_2 = self.findChild(QtWidgets.QComboBox, "c_2")
        self.c_3 = self.findChild(QtWidgets.QComboBox, "c_3")
        self.c_4 = self.findChild(QtWidgets.QComboBox, "c_4")
        self.c_5 = self.findChild(QtWidgets.QComboBox, "c_5")

        self.t_0 = self.findChild(QtWidgets.QComboBox, "t_0")
        self.t_1 = self.findChild(QtWidgets.QComboBox, "t_1")
        self.t_2 = self.findChild(QtWidgets.QComboBox, "t_2")
        self.t_3 = self.findChild(QtWidgets.QComboBox, "t_3")
        self.t_4 = self.findChild(QtWidgets.QComboBox, "t_4")
        self.t_5 = self.findChild(QtWidgets.QComboBox, "t_5")

        self.combo_pairs = {
            self.c_0: self.t_0,
            self.c_1: self.t_1,
            self.c_2: self.t_2,
            self.c_3: self.t_3,
            self.c_4: self.t_4,
            self.c_5: self.t_5,
        }

        for combo in self.combo_pairs:
            combo.addItem("Seleccione el tipo de honorario")
            combo.addItems(list(self.tratamientos.keys()))
            combo.currentTextChanged.connect(self.loadTratamientos)

    def loadTratamientos(self):
        sender = self.sender()

        selected_honorario = sender.currentText()

        if selected_honorario == "Seleccione el tipo de honorario":
            return

        conexion = sqlite3.connect('interfaces/database.db')
        cursor = conexion.cursor()

        linked_combo = self.combo_pairs[sender]
        linked_combo.clear()

        tratamientos_honorario = self.tratamientos.get(selected_honorario, [])

        for tratamiento in tratamientos_honorario:
            cursor.execute("SELECT monto FROM Trata WHERE tipo_tratamiento = ? AND tratamiento = ?", (selected_honorario, tratamiento))
            monto = cursor.fetchone()
            if monto:
                linked_combo.addItem(tratamiento)
                
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("si")

    SI = Ui_SI()
    SI.showFullScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(SI)
    widget.setGeometry(SI.geometry())

    widget.show()
    sys.exit(app.exec_())
